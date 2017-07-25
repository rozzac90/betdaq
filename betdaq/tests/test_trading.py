
import unittest
import unittest.mock as mock

from betdaq.apiclient import APIClient
from betdaq.enums import HeartbeatAction
from betdaq.endpoints.trading import Trading


class BettingTest(unittest.TestCase):

    def setUp(self):
        client = APIClient('username', 'password')
        self.trading = Trading(client)

    @mock.patch('betdaq.endpoints.trading.Trading.process_response')
    @mock.patch('betdaq.endpoints.trading.Trading.request', return_value=mock.Mock())
    def test_list_blacklist_information(self, mock_request, mock_process_response):
        self.trading.list_blacklist_information()

        mock_request.assert_called_once_with('ListBlacklistInformation', {}, secure=True)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.trading.Trading.process_response')
    @mock.patch('betdaq.endpoints.trading.Trading.request', return_value=mock.Mock())
    def test_suspend_from_trading(self, mock_request, mock_process_response):
        self.trading.suspend_from_trading()

        mock_request.assert_called_once_with('SuspendFromTrading', {}, secure=True)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.trading.Trading.process_response')
    @mock.patch('betdaq.endpoints.trading.Trading.request', return_value=mock.Mock())
    def test_unsuspend_from_trading(self, mock_request, mock_process_response):
        self.trading.unsuspend_from_trading()

        mock_request.assert_called_once_with('UnsuspendFromTrading', {}, secure=True)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.trading.Trading.process_response')
    @mock.patch('betdaq.endpoints.trading.Trading.request', return_value=mock.Mock())
    def test_register_heartbeat(self, mock_request, mock_process_response):
        self.trading.register_heartbeat(HeartbeatAction=HeartbeatAction.CancelOrders.value, ThresholdMs=6000)

        mock_request.assert_called_once_with(
            'RegisterHeartbeat', {'HeartbeatAction': 1, 'ThresholdMs': 6000}, secure=True
        )
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.trading.Trading.process_response')
    @mock.patch('betdaq.endpoints.trading.Trading.request', return_value=mock.Mock())
    def test_deregister_heartbeat(self, mock_request, mock_process_response):
        self.trading.deregister_heartbeat()

        mock_request.assert_called_once_with('DeregisterHeartbeat', {}, secure=True)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.trading.Trading.process_response')
    @mock.patch('betdaq.endpoints.trading.Trading.request', return_value=mock.Mock())
    def test_change_heartbeat(self, mock_request, mock_process_response):
        self.trading.change_hearbeat(HeartbeatAction=HeartbeatAction.CancelOrders.value, ThresholdMs=6000)

        mock_request.assert_called_once_with(
            'ChangeHeartbeatRegistration', {'HeartbeatAction': 1, 'ThresholdMs': 6000}, secure=True
        )
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.trading.Trading.process_response')
    @mock.patch('betdaq.endpoints.trading.Trading.request', return_value=mock.Mock())
    def test_send_pulse(self, mock_request, mock_process_response):
        self.trading.send_pulse()

        mock_request.assert_called_once_with('Pulse', {}, secure=True)
        assert mock_process_response.call_count == 1
