
from betdaq.utils import make_tz_naive, floatify


def parse_account_postings(posts):
    return {
            'postings_complete': posts.get('HaveAllPostingsBeenReturned'),
            'currency': posts.get('Currency'),
            'available_funds': floatify(posts.get('AvailableFunds')),
            'balance': floatify(posts.get('Balance')),
            'credit': floatify(posts.get('Credit')),
            'exposure': floatify(posts.get('Exposure')),
            'transactions': [{
                'transaction_time': make_tz_naive(order.get('PostedAt')),
                'description': order.get('Description'),
                'amount': floatify(order.get('Amount')),
                'resulting_balance': floatify(order.get('ResultingBalance')),
                'transaction_category': order.get('PostingCategory'),
                'order_id': order.get('OrderId'),
                'market_id': order.get('MarketId'),
                'transaction_id': order.get('TransactionId')
            } for order in posts.get('Orders', {}).get('Order', []) if posts.get('Orders')]
    } if posts.get('Orders') and posts.get('Orders', {}).get('Order', []) else {}


def parse_account_balance(bal):
    return {
        'currency': bal.get('Currency'),
        'available_funds': floatify(bal.get('AvailableFunds')),
        'balance': floatify(bal.get('Balance')),
        'credit': floatify(bal.get('Credit')),
        'exposure': floatify(bal.get('Exposure')),
    }
