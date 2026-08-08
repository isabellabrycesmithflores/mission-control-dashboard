# 🌐 Communication with external APIs

import requests
from datetime import datetime


def get_upcoming_launches():
    """Fetch upcoming launches from The Space Devs API."""

    url = "https://ll.thespacedevs.com/2.3.0/launches/upcoming/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.RequestException as error:
        print(f"Unable to retrieve launch data: {error}")
        return []

    data = response.json()

    launches = data["results"]

    return launches


def display_launches(launches):
    """Display upcoming launches in the terminal."""

    print()
    print("================================")
    print("     🚀 UPCOMING LAUNCHES")
    print("================================")

    for launch in launches:
        name = launch["name"]

        date = datetime.fromisoformat(
            launch["net"].replace("Z", "+00:00")
        )

        formatted_date = date.strftime("%d %B %Y • %H:%M")

        provider_data = launch.get("launch_service_provider")

        if provider_data:
            provider = provider_data.get("name", "Unknown Provider")
        else: 
            provider = "Unknown Provider"

        print(f"🚀 {name}")
        print(f"📅 {formatted_date}")
        print(f"🏢 {provider}")
        print("------------------------------")

    