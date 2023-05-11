
import bisect

from betdaq.utils import make_tz_naive, price_side_map, floatify
from betdaq.enums import MarketType, MarketStatus, SelectionStatus, Polarity


def parse_deep_markets(sports):
    markets = []
    for sport in sports:
        events = sport.get('EventClassifiers')
        sub_events = []
        while events:
            for event in events:
                markets += parse_market(
                    event.get('Markets', []), {'event_name': event.get('Name'),
                                               'tournament_id': event.get('tournament_id'),
                                               'tournament_name': event.get('tournament_name'),
                                               'competition_id': event.get('competition_id'),
                                               'competition_name': event.get('competition_name'),
                                               'sport_id': sport.get('Id'),
                                               'sport_name': sport.get('Name'),
                                               }
                )
                if event.get('EventClassifiers', []):
                    sub_events += [{**ev, **{'competition_name': event.get('Name')
                                             if event.get('tournament_name') and event.get('competition_name') is None
                                             else event.get('competition_name') if event.get('competition_name')
                                             else None,
                                             'competition_id': event.get('Id')
                                             if event.get('tournament_name') and event.get('competition_name') is None
                                             else event.get('competition_id') if event.get('competition_name')
                                             else None,
                                             'tournament_name': event.get('tournament_name', event.get('Name')),
                                             'tournament_id': event.get('tournament_id', event.get('Id')),
                                             }
                                    } for ev in event.get('EventClassifiers', [])]
            events = sub_events.copy()
            sub_events = []
    return markets


def parse_runners(data):
    return {'runner_id': data.get('Id'),
            'runner_name': data.get('Name'),
            'runner_status': SelectionStatus(int(data.get('Status'))).name if data.get('Status') else None,
            'reset_count': data.get('ResetCount'),
            'deduction_factor': floatify(data.get('DeductionFactor')),
            'runner_display_order': data.get('DisplayOrder')}


def parse_market(mkt_data, other_info):
    return [{**{'runners': [parse_runners(runner) for runner in mkt.get('Selections', [])],
                'market_id':  mkt.get('Id'),
                'market_name':  mkt.get('Name'),
                'market_type':  MarketType(int(mkt.get('Type'))).name if mkt.get('Type') else None,
                'is_play_market': mkt.get('IsPlayMarket'),
                'market_status': MarketStatus(int(mkt.get('Status'))).name if mkt.get('Status') else None,
                'number_of_winners': mkt.get('NumberOfWinningSelections'),
                'market_start_time': make_tz_naive(mkt.get('StartTime')),
                'withdrawal_sequence_number': mkt.get('WithdrawalSequenceNumber'),
                'market_display_order': mkt.get('DisplayOrder'),
                'enabled_for_multiples': mkt.get('IsEnabledForMultiples'),
                'in_play_available': mkt.get('IsInRunningAllowed'),
                'race_grade': mkt.get('RaceGrade'),
                'managed_in_running': mkt.get('IsManagedWhenInRunning'),
                'in_play': mkt.get('IsCurrentlyInRunning'),
                'in_play_delay': mkt.get('InRunningDelaySeconds'),
                'event_id': mkt.get('EventClassifierId'),
                'place_payout': floatify(mkt.get('PlacePayout'))},
             **other_info} for mkt in mkt_data]


def parse_sub_event(data, prefix='comp', parent='sport'):
    return {
        '%s_id' % prefix: data.get('Id'),
        '%s_name' % prefix: data.get('Name'),
        '%s_display_order' % prefix: data.get('DisplayOrder'),
        '%s_id' % parent: data.get('ParentId'),
        '%s_multi_allowed' % prefix: data.get('IsEnabledForMultiples'),
    }


def parse_market_prices(mkt):
    return {'market_id': mkt.get('Id'),
            'market_name': mkt.get('Name'),
            'market_type': MarketType(int(mkt.get('Type'))).name if mkt.get('Type') else None,
            'market_start_time': make_tz_naive(mkt.get('StartTime')),
            'runners': [parse_runner_prices(runner) for runner in mkt.get('Selections', [])],
            'is_play_market': mkt.get('IsPlayMarket'),
            'status': MarketStatus(int(mkt.get('Status'))) if mkt.get('Status') else None,
            'number_of_winners': floatify(mkt.get('NumberOfWinningSelections')),
            'withdrawal_sequence_number': mkt.get('WithdrawalSequenceNumber'),
            'market_display_order': mkt.get('DisplayOrder'),
            'enabled_for_multiples': mkt.get('IsEnabledForMultiples'),
            'in_play_available': mkt.get('IsInRunningAllowed'),
            'race_grade': mkt.get('RaceGrade'),
            'managed_in_running': mkt.get('IsManagedWhenInRunning'),
            'in_play': mkt.get('IsCurrentlyInRunning'),
            'in_running_delay': mkt.get('InRunningDelaySeconds'),
            'event_id': mkt.get('EventClassifierId'),
            'market_total_matched': floatify(mkt.get('TotalMatchedAmount')),
            'place_payout': floatify(mkt.get('PlacePayout')),
            'market_back_matched': floatify(mkt.get('MatchedMarketForStake')),
            'market_lay_matched': floatify(mkt.get('MatchedMarketAgainstStake')),
            'home_team_score': mkt.get('HomeTeamScore'),
            'away_team_score': mkt.get('AwayTeamScore'),
            'score_type': mkt.get('ScoreType'),
            }


def parse_runner_prices(runner):
    return {
        'runner_book': parse_runner_book(runner.get('_value_1', [])),
        'runner_id': runner.get('Id'),
        'runner_name': runner.get('Name'),
        'runner_status': SelectionStatus(int(runner.get('Status'))).name if runner.get('Status') else None,
        'runner_reset_count': floatify(runner.get('ResetCount')),
        'deduction_factor': floatify(runner.get('DeductionFactor')),
        'runner_back_matched_size': floatify(runner.get('MatchedSelectionForStake')),
        'runner_lay_matched_size': floatify(runner.get('MatchedSelectionAgainstStake')),
        'runner_last_matched_time': make_tz_naive(runner.get('LastMatchedOccurredAt')),
        'runner_last_matched_price': floatify(runner.get('LastMatchedPrice')),
        'runner_last_matched_back_size': floatify(runner.get('LastMatchedForSideAmount')),
        'runner_last_matched_lay_size': floatify(runner.get('LastMatchedAgainstSideAmount')),
        'runner_open_interest': floatify(runner.get('SelectionOpenInterest')),
        'runner_market_winnings': floatify(runner.get('MarketWinnings')),
        'runner_positive_winnings': floatify(runner.get('MarketPositiveWinnings')),
        'runner_back_matched_same_price': floatify(runner.get('MatchedForSideAmountAtSamePrice')),
        'runner_lay_matched_same_price': floatify(runner.get('MatchedAgainstSideAmountAtSamePrice')),
        'runner_last_traded_same_price': make_tz_naive(runner.get('FirstMatchAtSamePriceOccurredAt')),
        'runner_total_matched_orders': floatify(runner.get('NumberOrders')),
        'runner_total_matched_punters': floatify(runner.get('NumberPunters')),
        }


def parse_runner_book(book):
    back_levels = []
    lay_levels = []
    order_book = {'batb': [], 'batl': []}
    for level in book:
        for side, order in level.items():
            if order:
                side = price_side_map.get(side)
                if side == 'back':
                    bisect.insort(back_levels, floatify(order.get('Price')))
                    order_book['batb'].append([floatify(order.get('Price')), floatify(order.get('Stake'))])
                elif side == 'lay':
                    bisect.insort_right(lay_levels, floatify(order.get('Price')))
                    order_book['batl'].append([floatify(order.get('Price')), floatify(order.get('Stake'))])
    back_levels.reverse()
    order_book['batb'] = [[back_levels.index(x[0]), x[0], x[1]] for x in order_book['batb']]
    order_book['batl'] = [[lay_levels.index(x[0]), x[0], x[1]] for x in order_book['batl']]
    return order_book


def parse_selection_changes(chg):
    return {
        'runner_id': chg.get('Id'),
        'runner_name': chg.get('Name'),
        'runner_display_order': chg.get('DisplayOrder'),
        'runner_hidden': chg.get('IsHidden'),
        'runner_status': SelectionStatus(int(chg.get('Status'))) if chg.get('Status') else None,
        'reset_count': chg.get('ResetCount'),
        'market_id': chg.get('MarketId'),
        'withdrawal_factor': chg.get('WithdrawalFactor'),
        'sequence_number': chg.get('SelectionSequenceNumber'),
        'cancel_orders_time': make_tz_naive(chg.get('CancelOrdersTime')),
        'settlement_info': [{'settled_time': make_tz_naive(stl.get('SettlementInformation', {}).get('SettledTime')),
                             'void_percentage': stl.get('SettlementInformation', {}).get('VoidPercentage'),
                             'result': stl.get('SettlementInformation', {}).get('SettlementResultString'),
                             'left_side_percentage': stl.get('SettlementInformation', {}).get('LeftSideFactor'),
                             'right_side_percentage': stl.get('SettlementInformation', {}).get('RightSideFactor')
                             } for stl in chg.get('_value_1', [])]
    }


def parse_market_withdrawal(data):
    return {
        'runner_id': data.get('SelectionId'),
        'withdrawal_time': make_tz_naive(data.get('WithdrawalTime')),
        'sequence_number': data.get('SequenceNumber'),
        'reduction_factor': floatify(data.get('ReductionFactor')),
        'compound_reduction_factor': floatify(data.get('CompoundReductionFactor')),
    }


def parse_ladder(data):
    return [
        {'price': floatify(ol.get('price')),
         'value': ol.get('representation')} for ol in data]


def parse_sports(sport):
    return {'display_order': sport.get('DisplayOrder'),
            'sport_id': sport.get('Id'),
            'sport_name': sport.get('Name')}


def parse_trade_item(trade):
    trd = trade.get('TradeItems', {})
    return {
        'traded_time': make_tz_naive(trd.get('occurredAt')),
        'price': floatify(trd.get('price')),
        'size': floatify(trd.get('backersStake')),
        'side': Polarity(int(trd.get('tradeType'))).name if trd.get('tradeType') else None,
    }


def parse_selection_trades(trades):
    return {
        'runner_id': trades.get('selectionId'),
        'max_trade_id': trades.get('maxTradeId'),
        'max_trade_id_returned': trades.get('maxTradeIdReturned'),
        'trades': [parse_trade_item(t) for t in trades.get('_value_1', [])],
    }
