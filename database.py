
import sqlite3

def create_database():
    """Create the SQLite database and launches table."""

    connection = sqlite3.connect("mission_control.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS launches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        api_id TEXT UNIQUE,
        name TEXT,
        date TEXT,
        provider TEXT,
        status TEXT
    )
    """)

    connection.commit()

    return connection


def save_launches(connection, launches):
    """Save launch data into the database."""

    cursor = connection.cursor()

    for launch in launches:
        api_id = launch["id"]
        name = launch["name"]
        date = launch["net"]

        provider = launch.get("launch_service_provider")

        if provider:
            provider = provider.get("name", "Unknown provider")
        else:
            provider = "Unknown provider"

        cursor.execute("""
            INSERT OR IGNORE INTO launches
            (api_id, name, date, provider, status)
            VALUES (?, ?, ?, ?, ?)
        """, (api_id, name, date, provider, "Upcoming"))

    connection.commit()

connection = create_database()

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM launches")

count = cursor.fetchone()[0]

print(f"Launches stored in database: {count}")

connection.close()