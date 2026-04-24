# <img src="https://whatpulse.org/assets/images/favicon/favicon-96x96.png" width="40" style="vertical-align:middle;" /> what_pulse.py

> Web-API for [WhatPulse](https://whatpulse.org) a stats tracking app that measures your keyboard, mouse, network, and uptime activity. Retrieve user and team statistics via their public API.

</div>

## Quick Start
```python
from whatpulse import WhatPulse

wp = WhatPulse()

# Get stats for a user
print(wp.get_user_stats("ocsi01"))

# Get pulse history for a user
print(wp.get_user_pulse_stats("ocsi01"))

# Get stats for a team
print(wp.get_team_stats("WhatPulse"))
```

---

## User

| Method | Description |
|--------|-------------|
| `get_user_stats(user)` | Get stats for a user by username or ID |
| `get_user_pulse_stats(user)` | Get pulse history for a user |

---

## Team

| Method | Description |
|--------|-------------|
| `get_team_stats(team)` | Get stats for a team by name |
| `get_team_pulse_stats(team)` | Get pulse history for a team |
