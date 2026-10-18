# Mission Control Dashboard

A Python terminal app that tracks upcoming rocket launches from around the world.

**[🚀🪐✨ Try the live app! ✨🪐🚀](https://space-mission-control-dashboard-isabella.streamlit.app)**

## Features
This App:
- Fetches live launch data from The Space Devs API
- Shows each launch's name, date, provider & status
- Saves launches to a SQLite database and keeps them up to date when the launches are delayed
- Offline mode: shows the saved launches if the API can not be reached due to no wifi 

# Built with
- Python
- The Space Devs Launch Library 2 API
- SQLite
- Rich
- Streamlit
- https://htmlcolorcodes.com/color-wheel/ 


## What I used
- Python
- `requests` for calling the API
- SQLite for storing launch data
- Code split into modules (`api.py`, `database.py`, `main.py`,'app.py' )
- https://htmlcolorcodes.com/color-wheel/ For choosing colour codes

## How to run
```bash
pip install -r requirements.txt
python main.py

## Future ideas
- Countdown to the next launch
- Filter launches by provider
- Launch reminders
