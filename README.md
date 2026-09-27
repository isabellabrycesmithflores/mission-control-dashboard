# 🚀 Mission Control Dashboard

A Python terminal app that tracks upcoming rocket launches from around the world.

**[🚀 Try the live app](https://space-mission-control-dashboard-isabella.streamlit.app)**

## Features
- Fetches live launch data from The Space Devs API
- Shows each launch's name, date, provider and status
- Saves launches to a SQLite database and keeps them up to date when launches are delayed
- Offline mode: shows saved launches if the API can't be reached

## How to run
```bash
pip install -r requirements.txt
python main.py
```

## What I used
- Python
- `requests` for calling the API
- SQLite for storing launch data
- Code split into modules (`api.py`, `database.py`, `main.py`)

## Future ideas
- Countdown to the next launch
- Filter launches by provider (e.g. SpaceX)
- Launch reminders
