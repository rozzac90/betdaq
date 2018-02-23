
import unittest
import unittest.mock as mock
from collections import OrderedDict
from zeep.helpers import serialize_object

from betdaq.enums import Boolean, PriceFormat
from betdaq.apiclient import APIClient
from betdaq.endpoints.marketdata import MarketData


class BettingTest(unittest.TestCase):

    def setUp(self):
        client = APIClient('username', 'password')
        self.market_data = MarketData(client)

    @mock.patch('betdaq.endpoints.marketdata.MarketData.process_response')
    @mock.patch('betdaq.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_sports(self, mock_request, mock_process_response):
        self.market_data.get_sports()

        mock_request.assert_called_once_with('ListTopLevelEvents', {}, secure=False)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.marketdata.MarketData.process_response')
    @mock.patch('betdaq.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_sports_with_selections(self, mock_request, mock_process_response):
        self.market_data.get_sport_markets(
            sport_ids=[10005], include_selections=True, WantDirectDescendentsOnly=Boolean.F.value
        )

        method, args = mock_request.call_args
        params = serialize_object(method[1])

        assert method[0] == 'GetEventSubTreeWithSelections'
        assert params == OrderedDict({'_value_1': [OrderedDict({'EventClassifierIds': s_id}) for s_id in [10005]],
                                      'WantPlayMarkets': None})
        assert args['secure'] is False

        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.marketdata.MarketData.process_response')
    @mock.patch('betdaq.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_sports_without_selections(self, mock_request, mock_process_response):
        self.market_data.get_sport_markets(
            sport_ids=[10005], include_selections=False, WantDirectDescendentsOnly=Boolean.F.value
        )

        method, args = mock_request.call_args
        params = serialize_object(method[1])

        assert method[0] == 'GetEventSubTreeNoSelections'
        assert params == OrderedDict({'_value_1': [OrderedDict({'EventClassifierIds': s_id}) for s_id in [10005]],
                                     'WantDirectDescendentsOnly': 'false',  'WantPlayMarkets': None})
        assert args['secure'] is False

        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.marketdata.MarketData.process_response')
    @mock.patch('betdaq.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_markets(self, mock_request, mock_process_response):
        self.market_data.get_markets(market_ids=[12, 34])

        method, args = mock_request.call_args
        params = serialize_object(method[1])

        assert method[0] == 'GetMarketInformation'
        assert params == OrderedDict({'_value_1': [OrderedDict({'MarketIds': m_id}) for m_id in [12, 34]]})
        assert args['secure'] is False

        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.marketdata.MarketData.process_response')
    @mock.patch('betdaq.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_selection_changes(self, mock_request, mock_process_response):
        self.market_data.get_selection_changes(SelectionSequenceNumber=1)

        mock_request.assert_called_once_with('ListSelectionsChangedSince', {'SelectionSequenceNumber': 1}, secure=False)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.marketdata.MarketData.process_response')
    @mock.patch('betdaq.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_market_withdrawals(self, mock_request, mock_process_response):
        self.market_data.get_market_withdrawals(MarketId=1234)

        mock_request.assert_called_once_with('ListMarketWithdrawalHistory', {'MarketId': 1234}, secure=False)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.marketdata.MarketData.process_response')
    @mock.patch('betdaq.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_prices(self, mock_request, mock_process_response):
        self.market_data.get_prices(
            market_ids=[12, 34], ThresholdAmount=5.0, NumberForPricesRequired=-1, NumberAgainstPricesRequired=-1,
            WantMarketMatchedAmount=Boolean.T.value, WantSelectionsMatchedAmounts=Boolean.T.value,
            WantSelectionMatchedDetails=Boolean.T.value
        )

        method, args = mock_request.call_args
        params = serialize_object(method[1])
        assert method[0] == 'GetPrices'
        assert params == OrderedDict(
            {'_value_1': [OrderedDict({'MarketIds': m_id}) for m_id in [12, 34]], 'ThresholdAmount': 5.0,
             'NumberForPricesRequired': -1, 'NumberAgainstPricesRequired': -1, 'WantMarketMatchedAmount': 'true',
             'WantSelectionsMatchedAmounts': 'true', 'WantSelectionMatchedDetails': 'true'}
        )
        assert args['secure'] is False

        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.marketdata.MarketData.process_response')
    @mock.patch('betdaq.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_odds_ladder(self, mock_request, mock_process_response):
        self.market_data.get_odds_ladder(PriceFormat=PriceFormat.Decimal.value)

        mock_request.assert_called_once_with('GetOddsLadder', {'PriceFormat': 1}, secure=False)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.marketdata.MarketData.process_response')
    @mock.patch('betdaq.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_markets_with_sp(self, mock_request, mock_process_response):
        self.market_data.get_markets_with_sp()

        mock_request.assert_called_once_with('GetSPEnabledMarketsInformation', {}, secure=False)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.marketdata.MarketData.process_response')
    @mock.patch('betdaq.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_selection_sequence_number(self, mock_request, mock_process_response):
        self.market_data.get_selection_sequence_number()

        mock_request.assert_called_once_with('GetCurrentSelectionSequenceNumber', {}, secure=False)
        assert mock_process_response.call_count == 1

    @mock.patch('betdaq.endpoints.marketdata.MarketData.process_response')
    @mock.patch('betdaq.endpoints.marketdata.MarketData.request', return_value=mock.Mock())
    def test_get_selection_trades(self, mock_request, mock_process_response):
        self.market_data.get_selection_trades(
            selection_info=[{'selectionId': 1, 'fromTradeId': 1}, {'selectionId': 2}], currency='EUR'
        )

        method, args = mock_request.call_args
        params = serialize_object(method[1])
        assert method[0] == 'ListSelectionTrades'
        assert params == OrderedDict(
            {'_value_1': [OrderedDict({'selectionRequests': OrderedDict({'selectionId':  s_i.get('selectionId'),
                                                                         'fromTradeId': s_i.get('fromTradeId')})})
                          for s_i in [{'selectionId': 1, 'fromTradeId': 1}, {'selectionId': 2}]],
             'currency': 'EUR'}
        )
        assert args['secure'] is False

        assert mock_process_response.call_count == 1
