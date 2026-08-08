# 🚀 Mission Control Dashboard

from api import get_upcoming_launches, display_launches


print("================================")
print("       🚀 MISSION CONTROL")
print("================================")
print()

print("Connecting to Mission Control...")
print()

launches = get_upcoming_launches()

print(f"Upcoming launches tracked: {len(launches)}")

display_launches(launches)

def get_next_launch(launches):
    """Return the next upcoming launch."""

    if not launches:
        return None

    return launches[0]