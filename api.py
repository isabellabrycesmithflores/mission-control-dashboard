# 🌐 Communication with external APIs

import requests
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()


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

    return data["results"]


def display_launches(launches):
    """Display upcoming launches as a colourful table."""

    table = Table(title="🚀 Upcoming Launches", header_style="bold cyan")

    table.add_column("Mission", style="bold white")
    table.add_column("Date", style="green")
    table.add_column("Provider", style="magenta")
    table.add_column("Status")

    for launch in launches:
        name = launch["name"]

        date = datetime.fromisoformat(
            launch["net"].replace("Z", "+00:00")
        )
        formatted_date = date.strftime("%d %b %Y • %H:%M")

        provider_data = launch.get("launch_service_provider")

        if provider_data:
            provider = provider_data.get("name", "Unknown Provider")
        else:
            provider = "Unknown Provider"

        status = launch["status"]["name"]

        if status == "Go for Launch":
            colour = "green"
        elif "Confirmed" in status or "Determined" in status:
            colour = "yellow"
        else:
            colour = "white"

        table.add_row(name, formatted_date, provider, f"[{colour}]{status}[/]")

    console.print(table)