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

def get_spacex_launches(connection):
    """Get all SpaceX launches from the database."""

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM launches
        WHERE provider = ?
    """, ("SpaceX",))

    return cursor.fetchall()


def get_next_launch(connection):
    """Get the next upcoming launch from the database."""

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM launches
        WHERE status = ?
        ORDER BY date ASC
        LIMIT 1
    """, ("Upcoming",))

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
