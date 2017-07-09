from betdaq.baseclient import BaseClient
from betdaq import endpoints


class APIClient(BaseClient):

    def __init__(self, username, password):
        super(APIClient, self).__init__(username, password)

        self.betting = endpoints.Betting(self)
        self.account = endpoints.Account(self)
        self.marketdata = endpoints.MarketData(self)
        self.trading = endpoints.Trading(self)

    def __repr__(self):
        return '<APIClient [%s]>' % self.username

    def __str__(self):
        return 'APIClient'
