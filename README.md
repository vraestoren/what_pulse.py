# what_pulse.py
Web-API for [whatpulse.org](https://whatpulse.org) website that measures your keyboard/mouse usage

## Example
```python
from what_pulse import WhatPulse

wp = WhatPulse()
user_stats = wp.get_user_stats(user_id="")
print(user_stats)
```
