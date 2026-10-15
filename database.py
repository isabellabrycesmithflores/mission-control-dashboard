# This module handles the SQLite database for the mission control application. The database is used to also store launch information when the application is offline or when the API is unavailable.

import sqlite3

from datetime import datetime, timezone

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
    """Save launch data into the database, updating any that already exist."""

    cursor = connection.cursor()

    for launch in launches:
        api_id = launch["id"]
        name = launch["name"]
        date = launch["net"]
        status = launch["status"]["name"]

        provider = launch.get("launch_service_provider")

        if provider:
            provider = provider.get("name", "Unknown provider")
        else:
            provider = "Unknown provider"

        cursor.execute("""
            INSERT INTO launches (api_id, name, date, provider, status)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(api_id) DO UPDATE SET
                name = excluded.name,
                date = excluded.date,
                provider = excluded.provider,
                status = excluded.status
        """, (api_id, name, date, provider, status))

    connection.commit()


def get_next_launch(connection):
    """Get the next launch that hasn't happened yet."""

    cursor = connection.cursor()

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    cursor.execute("""
        SELECT name, date, provider FROM launches
        WHERE date >= ?
        ORDER BY date ASC
        LIMIT 1
    """, (now,))

    return cursor.fetchone()

def get_saved_launches(connection):
    """Load saved launches from the database, in the same shape as the API data."""

    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, date, provider, status FROM launches
        ORDER BY date ASC
    """)

    launches = []

    for name, date, provider, status in cursor.fetchall():
        launches.append({
            "name": name,
            "net": date,
            "launch_service_provider": {"name": provider},
            "status": {"name": status},
        })

    return launches
