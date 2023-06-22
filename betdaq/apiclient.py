from betdaq.baseclient import BaseClient
from betdaq import endpoints


class APIClient(BaseClient):

    def __init__(self, username: str, password: str, b2b: bool = False):
        super().__init__(username, password, b2b=b2b)

        self.betting = endpoints.Betting(self)
        self.account = endpoints.Account(self)
        self.marketdata = endpoints.MarketData(self)
        self.trading = endpoints.Trading(self)

    def __repr__(self):
        return '<APIClient [%s]>' % self.username

    def __str__(self):
        return 'APIClient'


class B2BBetdaqAPIClient(APIClient):
    def initialise_wsdl(self):
        self.wsdl_file = 'https://api.betdaqb2b.com/v2.0/API.wsdl'
        return super().initialise_wsdl()
