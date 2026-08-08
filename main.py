# 🚀 Mission Control Dashboard

from api import get_upcoming_launches, display_launches
from database import create_database, save_launches


print("================================")
print("       🚀 MISSION CONTROL")
print("================================")
print()

print("Connecting to Mission Control...")
print()

launches = get_upcoming_launches()

connection = create_database()

save_launches(connection, launches)

connection.close()

print(f"Upcoming launches tracked: {len(launches)}")

display_launches(launches)