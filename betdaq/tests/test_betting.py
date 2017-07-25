
import unittest
import unittest.mock as mock
from zeep.helpers import serialize_object

from betdaq.enums import Boolean
from betdaq.apiclient import APIClient
from betdaq.endpoints.betting import Betting


class BettingTest(unittest.TestCase):

    def setUp(self):
        client = APIClient('username', 'password')
        self.betting = Betting(client)

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_get_orders(self, mock_request, mock_process_response):
        self.betting.get_orders(SequenceNumber=-1, wantSettledOrdersOnUnsettledMarkets=Boolean.T.value)

        mock_request.assert_called_once_with(
            'ListBootstrapOrders', {'SequenceNumber': -1, 'wantSettledOrdersOnUnsettledMarkets': 'true'}, secure=True
        )
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_get_orders_diff(self, mock_request, mock_process_response):
        self.betting.get_orders_diff(SequenceNumber=100)

        mock_request.assert_called_once_with('ListOrdersChangedSince', {'SequenceNumber': 100}, secure=True)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_get_single_order(self, mock_request, mock_process_response):
        self.betting.get_single_order(OrderId=1)

        mock_request.assert_called_once_with('GetOrderDetails', {'OrderId': 1}, secure=True)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_place_orders_with_receipt(self, mock_request, mock_process_response):
        self.betting.place_orders(order_list=[], WantAllOrNothingBehaviour=Boolean.T.value, receipt=True)

        method, args = mock_request.call_args
        params = serialize_object(method[1])

        assert method[0] == 'PlaceOrdersWithReceipt'
        assert dict(params) == {'Orders': {'Order': []}}
        assert args['secure'] is True

        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_place_orders_without_receipt(self, mock_request, mock_process_response):
        self.betting.place_orders(order_list=[], WantAllOrNothingBehaviour=Boolean.T.value, receipt=False)

        method, args = mock_request.call_args
        params = serialize_object(method[1])

        assert method[0] == 'PlaceOrdersNoReceipt'
        assert dict(params) == {'Orders': {'Order': []}, 'WantAllOrNothingBehaviour': 'true'}
        assert args['secure'] is True

        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_update_orders(self, mock_request, mock_process_response):
        self.betting.update_orders(order_list=[])

        method, args = mock_request.call_args
        params = serialize_object(method[1])

        assert method[0] == 'UpdateOrdersNoReceipt'
        assert dict(params) == {'Orders': {'Order': []}}
        assert args['secure'] is True

        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_cancel_orders(self, mock_request, mock_process_response):
        self.betting.cancel_orders(order_ids=[1, 2])

        method, args = mock_request.call_args
        params = serialize_object(method[1])

        assert method[0] == 'CancelOrders'
        assert dict(params) == {'_value_1': [{'OrderHandle': order_id} for order_id in [1, 2]]}
        assert args['secure'] is True

        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_cancel_orders_by_market(self, mock_request, mock_process_response):
        self.betting.cancel_orders_by_market(market_ids=[123, 456])

        method, args = mock_request.call_args
        params = serialize_object(method[1])

        assert method[0] == 'CancelAllOrdersOnMarket'
        assert dict(params) == {'_value_1': [{'MarketIds': m_id} for m_id in [123, 456]]}
        assert args['secure'] is True

        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_cancel_all_orders(self, mock_request, mock_process_response):
        self.betting.cancel_all_orders()

        mock_request.assert_called_once_with('CancelAllOrders', {}, secure=True)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_suspend_orders(self, mock_request, mock_process_response):
        self.betting.suspend_orders(order_ids=[1, 2])

        method, args = mock_request.call_args
        params = serialize_object(method[1])

        assert method[0] == 'SuspendOrders'
        assert dict(params) == {'_value_1': [{'OrderIds': order_id} for order_id in [1, 2]]}
        assert args['secure'] is True

        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_suspend_orders_by_market(self, mock_request, mock_process_response):
        self.betting.suspend_orders_by_market(MarketId=123)

        mock_request.assert_called_once_with('SuspendAllOrdersOnMarket', {'MarketId': 123}, secure=True)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_suspend_all_orders(self, mock_request, mock_process_response):
        self.betting.suspend_all_orders()

        mock_request.assert_called_once_with('SuspendAllOrders', {}, secure=True)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.betting.Betting.process_response')
    @mock.patch('betdaq.endpoints.betting.Betting.request', return_value=mock.Mock())
    def test_unsuspend_orders(self, mock_request, mock_process_response):
        self.betting.unsuspend_orders(order_ids=[1, 2])

        method, args = mock_request.call_args
        params = serialize_object(method[1])

        assert method[0] == 'UnsuspendOrders'
        assert dict(params) == {'_value_1': [{'OrderIds': order_id} for order_id in [1, 2]]}
        assert args['secure'] is True

        assert mock_process_response.call_count == 1
