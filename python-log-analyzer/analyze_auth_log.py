import csv
import re
import sqlite3
from collections import Counter
from pathlib import Path


FAILED_PASSWORD_PATTERN = re.compile(
    r"^(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+"
    r"(?P<host>\S+)\s+"
    r"(?P<service>sshd(?:-session)?)\[\d+\]:\s+"
    r"Failed password for\s+"
    r"(?:(invalid user)\s+)?"
    r"(?P<user>\S+)\s+from\s+"
    r"(?P<src_ip>\d{1,3}(?:\.\d{1,3}){3})\s+"
    r"port\s+(?P<src_port>\d+)\s+ssh2"
)

ACCEPTED_PASSWORD_PATTERN = re.compile(
    r"^(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+"
    r"(?P<host>\S+)\s+"
    r"(?P<service>sshd(?:-session)?)\[\d+\]:\s+"
    r"Accepted password for\s+"
    r"(?P<user>\S+)\s+from\s+"
    r"(?P<src_ip>\d{1,3}(?:\.\d{1,3}){3})\s+"
    r"port\s+(?P<src_port>\d+)\s+ssh2"
)


def parse_auth_log(log_path):
    events = []

    with log_path.open("r", encoding="utf-8", errors="ignore") as file:
        for line_number, line in enumerate(file, start=1):
            failed_match = FAILED_PASSWORD_PATTERN.search(line)
            accepted_match = ACCEPTED_PASSWORD_PATTERN.search(line)

            if failed_match:
                events.append({
                    "line_number": line_number,
                    "timestamp": failed_match.group("timestamp"),
                    "host": failed_match.group("host"),
                    "user": failed_match.group("user"),
                    "src_ip": failed_match.group("src_ip"),
                    "src_port": failed_match.group("src_port"),
                    "event_type": "failed_ssh_login",
                    "raw_line": line.strip(),
                })

            elif accepted_match:
                events.append({
                    "line_number": line_number,
                    "timestamp": accepted_match.group("timestamp"),
                    "host": accepted_match.group("host"),
                    "user": accepted_match.group("user"),
                    "src_ip": accepted_match.group("src_ip"),
                    "src_port": accepted_match.group("src_port"),
                    "event_type": "successful_ssh_login",
                    "raw_line": line.strip(),
                })

    return events


def write_csv(events, output_path):
    fieldnames = [
        "line_number",
        "timestamp",
        "host",
        "user",
        "src_ip",
        "src_port",
        "event_type",
        "raw_line",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)


def write_sqlite(events, db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS auth_events")

    cursor.execute("""
        CREATE TABLE auth_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            line_number INTEGER,
            timestamp TEXT,
            host TEXT,
            user TEXT,
            src_ip TEXT,
            src_port INTEGER,
            event_type TEXT,
            raw_line TEXT
        )
    """)

    for event in events:
        cursor.execute("""
            INSERT INTO auth_events (
                line_number,
                timestamp,
                host,
                user,
                src_ip,
                src_port,
                event_type,
                raw_line
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            event["line_number"],
            event["timestamp"],
            event["host"],
            event["user"],
            event["src_ip"],
            int(event["src_port"]),
            event["event_type"],
            event["raw_line"],
        ))

    connection.commit()
    connection.close()


def find_failed_to_success_patterns(events):
    patterns = []

    failed_events = [
        event for event in events
        if event["event_type"] == "failed_ssh_login"
    ]

    successful_events = [
        event for event in events
        if event["event_type"] == "successful_ssh_login"
    ]

    for success in successful_events:
        related_failures = [
            failed for failed in failed_events
            if failed["user"] == success["user"]
            and failed["src_ip"] == success["src_ip"]
            and failed["line_number"] < success["line_number"]
        ]

        if related_failures:
            patterns.append({
                "user": success["user"],
                "src_ip": success["src_ip"],
                "failed_attempts_before_success": len(related_failures),
                "success_line_number": success["line_number"],
                "success_timestamp": success["timestamp"],
            })

    return patterns

def classify_risk(event):
    if event["event_type"] == "successful_ssh_login":
        return "Low"

    if event["event_type"] == "failed_ssh_login":
        if event["user"] in ["root", "admin", "administrator"]:
            return "High"
        return "Medium"

    return "Low"


def split_timestamp(timestamp):
    parts = timestamp.split()

    if len(parts) == 3:
        month = parts[0]
        day = parts[1]
        time_value = parts[2]
        event_date = f"{month} {day}"
        return event_date, time_value

    return timestamp, ""


def write_powerbi_csv(events, output_path):
    fieldnames = [
        "event_date",
        "event_time",
        "timestamp_raw",
        "host",
        "user",
        "src_ip",
        "src_port",
        "event_type",
        "risk_level",
        "event_category",
        "event_count",
    ]

    rows = []

    for event in events:
        event_date, event_time = split_timestamp(event["timestamp"])

        rows.append({
            "event_date": event_date,
            "event_time": event_time,
            "timestamp_raw": event["timestamp"],
            "host": event["host"],
            "user": event["user"],
            "src_ip": event["src_ip"],
            "src_port": event["src_port"],
            "event_type": event["event_type"],
            "risk_level": classify_risk(event),
            "event_category": "Authentication",
            "event_count": 1,
        })

    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def print_summary(events):
    failed_events = [
        event for event in events
        if event["event_type"] == "failed_ssh_login"
    ]

    successful_events = [
        event for event in events
        if event["event_type"] == "successful_ssh_login"
    ]

    top_failed_ips = Counter(event["src_ip"] for event in failed_events)
    targeted_users = Counter(event["user"] for event in failed_events)
    successful_users = Counter(event["user"] for event in successful_events)

    print("\n=== SSH Authentication Summary ===")
    print(f"Total parsed events: {len(events)}")
    print(f"Failed SSH login attempts: {len(failed_events)}")
    print(f"Successful SSH logins: {len(successful_events)}")

    print("\nTop failed source IPs:")
    for ip, count in top_failed_ips.most_common(10):
        print(f"- {ip}: {count}")

    print("\nTargeted users in failed attempts:")
    for user, count in targeted_users.most_common(10):
        print(f"- {user}: {count}")

    print("\nSuccessful SSH users:")
    for user, count in successful_users.most_common(10):
        print(f"- {user}: {count}")

    patterns = find_failed_to_success_patterns(events)

    print("\nFailed-to-success patterns:")
    if not patterns:
        print("- No failed-to-success patterns found.")
    else:
        for pattern in patterns:
            print(
                f"- User {pattern['user']} from {pattern['src_ip']} "
                f"had {pattern['failed_attempts_before_success']} failed attempt(s) "
                f"before successful login at {pattern['success_timestamp']}."
            )


def main():
    base_dir = Path(__file__).resolve().parent
    log_path = base_dir / "sample_auth.log"
    output_dir = base_dir / "output"
    output_dir.mkdir(exist_ok=True)

    output_csv = output_dir / "ssh_auth_events.csv"
    output_powerbi_csv = output_dir / "security_events_for_powerbi.csv"
    output_db = output_dir / "auth_events.db"

    if not log_path.exists():
        print(f"ERROR: Log file not found: {log_path}")
        return

    events = parse_auth_log(log_path)

    if not events:
        print("WARNING: No SSH authentication events were parsed.")
        print("Check whether sample_auth.log contains lines with:")
        print("- Failed password for ... from ... port ... ssh2")
        print("- Accepted password for ... from ... port ... ssh2")
        return

    print_summary(events)
    write_csv(events, output_csv)
    write_sqlite(events, output_db)
    write_powerbi_csv(events, output_powerbi_csv)
    print(f"\nCSV report saved to: {output_csv}")
    print(f"Power BI CSV saved to: {output_powerbi_csv}")
    print(f"SQLite database saved to: {output_db}")

if __name__ == "__main__":
    main()