
from betdaq.classifiers.marketdata import parse_classifier
from betdaq.utils import get_tag, get_attribs, listy_mc_list


def err_cancel_market(response):
    err_data = parse_classifier(response.get('_raw_elements', []), 'Order')
    response['Order'] = listy_mc_list(response.get('Order', [])) + err_data
    return response


def err_suspend_orders(response):
    err_data = parse_classifier(response.get('_raw_elements', []), 'Orders')
    response['Orders'] = listy_mc_list(response.get('Orders', [])) + err_data
    return response
