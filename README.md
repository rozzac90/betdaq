# betdaq
Python wrapper for Betdaq API.

[Betdaq Documentation](http://api.betdaq.com/v2.0/Docs/default.aspx)

# Installation

```bash
pip install git+https://github.com/tavkhelidzeluka/betdaq.git
```

# Usage

```python
from betdaq.apiclient import APIClient

api = APIClient('username', 'password')
sport_ids = api.marketdata.get_sports()
all_markets = api.marketdata.get_sports_markets([100005]) 
```
