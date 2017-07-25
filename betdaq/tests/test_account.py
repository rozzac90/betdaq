
import datetime
import unittest
import unittest.mock as mock

from betdaq.apiclient import APIClient
from betdaq.endpoints.account import Account


class AccountTest(unittest.TestCase):

    def setUp(self):
        client = APIClient('username', 'password')
        self.account = Account(client)

    @mock.patch('betdaq.endpoints.account.Account.process_response')
    @mock.patch('betdaq.endpoints.account.Account.request', return_value=mock.Mock())
    def test_get_account_balances(self, mock_request, mock_process_response):
        self.account.get_account_balances()

        mock_request.assert_called_once_with('GetAccountBalances', {}, secure=True)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.account.Account.process_response')
    @mock.patch('betdaq.endpoints.account.Account.request', return_value=mock.Mock())
    def test_get_account_transactions(self, mock_request, mock_process_response):
        self.account.get_account_transactions(StartTime=datetime.datetime(2017, 1, 1).timestamp(),
                                              EndTime=datetime.datetime(2017, 1, 10).timestamp())

        mock_request.assert_called_once_with(
            'ListAccountPostings', {'StartTime': 1483228800.0, 'EndTime': 1484006400.0}, secure=True
        )
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.account.Account.process_response')
    @mock.patch('betdaq.endpoints.account.Account.request', return_value=mock.Mock())
    def test_get_account_transactions_by_id(self, mock_request, mock_process_response):
        self.account.get_account_transactions_by_id(TransactionId=1)

        mock_request.assert_called_once_with('ListAccountPostingsById', {'TransactionId': 1}, secure=True)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.account.Account.process_response')
    @mock.patch('betdaq.endpoints.account.Account.request', return_value=mock.Mock())
    def test_change_account_password(self, mock_request, mock_process_response):
        self.account.change_account_password(Password='new_password')

        mock_request.assert_called_once_with('ChangePassword', {'Password': 'new_password'}, secure=True)
        assert mock_process_response.call_count == 1
