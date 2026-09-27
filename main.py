# 🚀 Mission Control Dashboard

from api import get_upcoming_launches, display_launches
from database import create_database, save_launches, get_saved_launches


print("================================")
print("       🚀 MISSION CONTROL")
print("================================")
print()

print("Connecting to Mission Control...")
print()

launches = get_upcoming_launches()

connection = create_database()

if launches:
    save_launches(connection, launches)
else:
    print("📴 Offline mode: showing saved launches")
    launches = get_saved_launches(connection)

connection.close()

print(f"Upcoming launches tracked: {len(launches)}")

display_launches(launches)

