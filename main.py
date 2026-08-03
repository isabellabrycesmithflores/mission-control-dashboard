# 🚀 Mission Control Dashboard

missions = [
    {
        "name": "Artemis II",
        "destination": "Moon",
        "crew": 4,
        "status": "In preparation"
    },
    {
        "name": "Europa Clipper",
        "destination": "Jupiter",
        "crew": 0,
        "status": "Active"
    },
    {
        "name": "Mars Sample Return",
        "destination": "Mars",
        "crew": 0,
        "status": "Planning"
    }
]

print("================================")
print("       🚀 MISSION CONTROL")
print("================================")
print()

for mission in missions:
    print(f"Mission: {mission['name']}")
    print(f"Destination: {mission['destination']}")
    print(f"Crew: {mission['crew']}")
    print(f"Status: {mission['status']}")
    print("--------------------------------")
    print()
print("MISSION SUMMARY")
print("--------------------------------")

total_missions = len(missions)
active_missions = 0

for mission in missions:
    if mission["status"] == "Active":
        active_missions += 1

print(f"Total missions: {total_missions}")
print(f"Active missions: {active_missions}")