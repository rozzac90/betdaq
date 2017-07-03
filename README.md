# betdaq_py
Python wrapper for Betdaq API.

[Documentation](http://api.betdaq.com/v2.0/Docs/default.aspx)

# Installation

```
$ python setup.py install
```

# Usage

```python
>>> from betdaq_py.apiclient import APIClient

>>> api = APIClient('username', 'password')

>>> sport_ids = api.marketdata.get_sports()

>>> all_markets = api.marketdata.get_sports_markets([100005]) 
```
