
from betdaq.classifiers.marketdata import (
    parse_classifier, parse_event_classfiers, parse_market_classifier, parse_selection_sequence_classifier,
    parse_selection_trades_classifier,
)
from betdaq.utils import get_attribs, get_tag, listy_mc_list


def err_selection_trades(response):
    err_data = parse_selection_trades_classifier(response.get('_raw_elements', []))
    response['SelectionTrades'] = listy_mc_list(response.get('SelectionTrades')) + err_data
    return response


def err_mkt_info(response):
    err_data = parse_market_classifier(response.get('_raw_elements', []))
    response['Markets'] = listy_mc_list(response.get('Markets', [])) + err_data.get('Markets', [])
    return response


def err_selection_changes(response):
    err_data = parse_selection_sequence_classifier(response.get('_raw_elements', []))
    response['Selections'] = listy_mc_list(response.get('Selections', [])) + err_data
    return response


def err_withdrawals(response):
    err_data = parse_classifier(response.get('_raw_elements', []), 'Withdrawals')
    response['Withdrawals'] = listy_mc_list(response.get('Withdrawals', [])) + err_data
    return response


def err_sport_markets(response):
    err_data = [
        {**get_attribs(mkt),
         **parse_market_classifier(mkt),
         **{'EventClassifiers': parse_event_classfiers(mkt)}} for mkt in response.get('_raw_elements', [])
    ]
    response['EventClassifiers'] = listy_mc_list(response.get('EventClassifiers', [])) + err_data
    return response


def err_sp_events(response):
    err_data = [
        {**get_attribs(child), **{'MarketTypeIds': {'MarketTypeId': sub_child.values()}
                                  for sub_child in child}} for child in response.get('_raw_elements', [])
    ]
    response['SPEnabledEvent'] = listy_mc_list(response.get('SPEnabledEvent', [])) + err_data
    return response


def err_prices(response):
    err_data = [
        {**get_attribs(mkt_prc),
         **{"Selections": [{**get_attribs(sel),
                            **{'_value_1': [{get_tag(prc): get_attribs(prc)} for prc in sel]}}
                           for sel in mkt_prc]}} for mkt_prc in response.get('_raw_elements', [])
    ]
    response['MarketPrices'] = [response['MarketPrices']] + err_data
    return response


def err_sports(response):
    err_data = [{**get_attribs(mkt), **parse_market_classifier(mkt)} for mkt in response.get('_raw_elements', [])]
    response['EventClassifiers'] = [response['EventClassifiers']] + err_data
    return response

