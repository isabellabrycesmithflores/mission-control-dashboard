# 🌐 Communication with external APIs

from abc import ABC, abstractmethod
from datetime import datetime

import requests


class RequestsAPI(ABC):
    """Abstract base class for external API request handlers."""

    @abstractmethod
    def get(self, endpoint: str, params: dict | None = None, timeout: int = 10) -> requests.Response:
        raise NotImplementedError

    @abstractmethod
    def get_upcoming_launches(self) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def display_launches(self, launches: list[dict]) -> None:
        raise NotImplementedError


class Requests(RequestsAPI):
    """Concrete implementation for The Space Devs API."""

    BASE_URL = "https://ll.thespacedevs.com/2.3.0"

    def get(self, endpoint: str, params: dict | None = None, timeout: int = 10) -> requests.Response:
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return response

    def get_upcoming_launches(self) -> list[dict]:
        response = self.get("/launches/upcoming/")
        data = response.json()
        return data.get("results", [])

    def display_launches(self, launches: list[dict]) -> None:
        print()
        print("================================")
        print("     🚀 UPCOMING LAUNCHES")
        print("================================")
        print()

        if not launches:
            print("No upcoming launches found.")
            return

        for launch in launches:
            name = launch.get("name", "Unknown")
            net = launch.get("net", "Unknown")
            provider = launch.get("launch_service_provider", {}).get("name", "Unknown")

            print(f"🚀 {name}")
            print(f"📅 {self._format_launch_date(net)}")
            print(f"🏢 {provider}")
            print("--------------------------------")

    def _format_launch_date(self, net: str) -> str:
        try:
            parsed_date = datetime.fromisoformat(net.replace("Z", "+00:00"))
            return parsed_date.strftime("%Y-%m-%d %H:%M UTC")
        except ValueError:
            return net


default_requests = Requests()


def get_upcoming_launches() -> list[dict]:
    """Fetch upcoming launches from The Space Devs API."""
    return default_requests.get_upcoming_launches()


def display_launches(launches: list[dict]) -> None:
    """Display upcoming launches in the terminal."""
    default_requests.display_launches(launches)
