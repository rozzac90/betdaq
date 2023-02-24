import zeep
from zeep import Settings


class BaseClient:
    def __init__(self, username: str, password: str, b2b: bool = False):
        self.username = username
        self.password = password
        self.wsdl_file = 'https://api.betdaq.com/v2.0/API.wsdl' if not b2b \
            else 'https://api.betdaqb2b.com/v2.0/API.wsdl'
        self.readonly_types = None
        self.secure_types = None
        self.secure_client, self.readonly_client = self.initialise_wsdl()
        self.initialise_type_factories()

    def initialise_wsdl(self):
        """
        Inspect the WSDL document and generates the corresponding code to use the services and types in the document.
        
        :return: client with available endpoints mapped.
        :rtype: zeep.Client
        """
        settings = Settings(strict=False)
        secure_client = zeep.Client(
            wsdl=self.wsdl_file, service_name='SecureService', port_name='SecureService', settings=settings
        )
        secure_client.set_default_soapheaders({'ExternalApiHeader': self.external_headers})
        readonly_client = zeep.Client(
            wsdl=self.wsdl_file, service_name='ReadOnlyService', port_name='ReadOnlyService', settings=settings
        )
        readonly_client.set_default_soapheaders({'ExternalApiHeader': self.external_headers})
        return secure_client, readonly_client

    def initialise_type_factories(self):
        self.readonly_types = self.readonly_client.type_factory('ns0')
        self.secure_types = self.secure_client.type_factory('ns0')

    @property
    def external_headers(self):
        return {"version": 2.0,
                "languageCode": 'en',
                "username": self.username,
                "password": self.password,
                "applicationIdentifier": None}
