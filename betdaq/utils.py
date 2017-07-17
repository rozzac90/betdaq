
import pytz
import datetime
from decimal import Decimal
from dateutil.parser import parse
from betdaq.enums import ErrorMap


def get_tag(elem):
    return elem.tag.split('}')[-1]


def get_attribs(elem):
    return {k: v for k, v in elem.attrib.items()}


def listy_mc_list(maybe_list):
    if maybe_list:
        return maybe_list if isinstance(maybe_list, list) else [maybe_list]
    else:
        return []


price_side_map = {
    'ForSidePrices': 'back',
    'AgainstSidePrices': 'lay',
    1: 'back',
    2: 'lay',
}


def parse_time_str(time_str):
    return parse(time_str)


def make_tz_naive(date):
    if isinstance(date, str):
        try:
            date = parse_time_str(date).strftime('%Y-%m-%d %H:%M:%S.%f')
        except:
            pass
    if isinstance(date, datetime.datetime):
        date = date.astimezone(pytz.UTC).replace(tzinfo=None).strftime('%Y-%m-%d %H:%M:%S.%f')
    return date


def clean_locals(params):
    """
    Clean up locals dict, remove empty and self params.

    :param params: locals dicts from a function.
    :type params: dict
    :returns: cleaned locals dict to use as params for functions
    :rtype: dict
    """
    return dict((k, v) for k, v in params.items() if v is not None and k != 'self')


def check_status_code(response, codes=None):
    """Checks response status_code is in codes
    :param response: Requests response
    :param codes: List of accepted codes or callable
    :raises: StatusCodeError if code invalid
    """
    codes = codes or [0]
    response_code = response.get('ReturnStatus', {}).get('Code')
    if response_code not in codes:
        raise eval(ErrorMap(response_code).name)


def floatify(deci):
    if isinstance(deci, Decimal) or isinstance(deci, str):
        return float(deci)
    else:
        return deci
