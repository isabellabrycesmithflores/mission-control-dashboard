# 🚀 Mission Control Dashboard - web app version

from datetime import datetime, timezone

import streamlit as st

from api import get_upcoming_launches
from database import create_database, save_launches, get_saved_launches


st.set_page_config(page_title="Mission Control", page_icon="🚀", layout="wide")

st.title("🚀 Mission Control")
st.caption("Live tracker for upcoming rocket launches around the world")


@st.cache_data(ttl=600)
def load_launches():
    """Get launches from the API, or from the database if offline."""

    launches = get_upcoming_launches()
    connection = create_database()

    if launches:
        save_launches(connection, launches)
        offline = False
    else:
        launches = get_saved_launches(connection)
        offline = True

    connection.close()
    return launches, offline


def get_provider(launch):
    provider = launch.get("launch_service_provider")
    if provider:
        return provider.get("name", "Unknown provider")
    return "Unknown provider"


launches, offline = load_launches()

if offline:
    st.warning("📴 Offline mode: showing saved launches")

# Only keep launches that haven't happened yet
now = datetime.now(timezone.utc)
upcoming = []

for launch in launches:
    date = datetime.fromisoformat(launch["net"].replace("Z", "+00:00"))
    if date >= now:
        upcoming.append((launch, date))

upcoming.sort(key=lambda item: item[1])

# Countdown section
if upcoming:
    next_launch, next_date = upcoming[0]
    time_left = next_date - now
    days = time_left.days
    hours = time_left.seconds // 3600

    col1, col2, col3 = st.columns(3)
    col1.metric("Next launch", next_launch["name"].split("|")[-1].strip())
    col2.metric("Countdown", f"{days}d {hours}h")
    col3.metric("Launches tracked", len(upcoming))

st.divider()

# Filter
providers = sorted({get_provider(launch) for launch, date in upcoming})
choice = st.selectbox("Filter by provider", ["All"] + providers)

# Launch cards
for launch, date in upcoming:
    provider = get_provider(launch)

    if choice != "All" and provider != choice:
        continue

    with st.container(border=True):
        picture, details = st.columns([1, 4])

        image = launch.get("image")
        if isinstance(image, dict) and image.get("thumbnail_url"):
            picture.image(image["thumbnail_url"])
        else:
            picture.markdown("# 🚀")

        details.subheader(launch["name"])
        details.write(f"📅 {date.strftime('%d %B %Y • %H:%M')} UTC")
        details.write(f"🏢 {provider}")
        details.write(f"📡 {launch['status']['name']}")
