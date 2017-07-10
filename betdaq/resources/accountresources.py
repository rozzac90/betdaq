
from betdaq.utils import make_tz_naive


def parse_account_postings(posts):
    return {
            'postings_complete': posts.get('HaveAllPostingsBeenReturned'),
            'currency': posts.get('Currency'),
            'available_funds': posts.get('AvailableFunds'),
            'balance': posts.get('Balance'),
            'credit': posts.get('Credit'),
            'exposure': posts.get('Exposure'),
            'transactions': [{
                'transaction_time': make_tz_naive(order.get('PostedAt')),
                'description': order.get('Description'),
                'amount': order.get('Amount'),
                'resulting_balance': order.get('ResultingBalance'),
                'transaction_category': order.get('PostingCategory'),
                'order_id': order.get('OrderId'),
                'market_id': order.get('MarketId'),
                'transaction_id': order.get('TransactionId')
            } for order in posts.get('Orders', {}).get('Order', []) if posts.get('Orders')]
    } if posts.get('Orders') and posts.get('Orders', {}).get('Order', []) else {}


def parse_account_balance(bal):
    return {
        'currency': bal.get('Currency'),
        'available_funds': bal.get('AvailableFunds'),
        'balance': bal.get('Balance'),
        'credit': bal.get('Credit'),
        'exposure': bal.get('Exposure'),
    }
