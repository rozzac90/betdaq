
from betdaq.utils import get_attribs, get_tag


def parse_selection_trades_classifier(elem):
    return [
        {**get_attribs(e), **{'_value_1': [{'TradeItems': t} for t in parse_classifier(e, 'TradeItems')]}}
        for e in elem if get_tag(e) == 'SelectionTrades'
    ]


def parse_selection_sequence_classifier(elem):
    return [
        {**get_attribs(e), **{'_value_1': [
            {'SettlementInformation': s_info} for s_info in parse_classifier(e, 'SettlementInformation')]}}
        for e in elem if get_tag(e) == 'Selections']


def parse_event_classfiers(elem):
    return [
        {**get_attribs(e), **parse_market_classifier(e),
         **{'EventClassifiers': [
             {**get_attribs(t), **parse_market_classifier(t),
              **{'EventClassifiers': [
                  {**get_attribs(c), **parse_market_classifier(c),
                   **{'EventClassifiers': [{**get_attribs(g), **parse_market_classifier(g)}
                                           for g in c if get_tag(g) == 'EventClassifiers']}}
                  for c in t if get_tag(c) == 'EventClassifiers']}}
             for t in e if get_tag(t) == 'EventClassifiers']}}
        for e in elem if get_tag(e) == 'EventClassifiers']


def parse_market_classifier(elem):
    return {'Markets': [{**get_attribs(e), **{'Selections': parse_classifier(e, 'Selections')}}
                        for e in elem if get_tag(e) == 'Markets']}


def parse_classifier(elem, name):
    return [get_attribs(e) for e in elem if get_tag(e) == name]
