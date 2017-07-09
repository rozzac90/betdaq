
from betdaq.utils import make_tz_naive
from betdaq.enums import OrderActionType, OrderStatus, OrderKillType, Polarity, MarketStatus


def parse_suspended_order(suspend):
    return {
        'order_id': suspend.get('OrderId'),
        'size_suspended': suspend.get('SuspendedForSideStake'),
        'customer_reference': suspend.get('PunterReferenceNumber'),
    }


def parse_cancelled_order(cancel):
    return {
        'order_id': cancel.get('OrderHandle'),
        'size_cancelled': cancel.get('cancelledForSideStake'),
        'customer_reference': cancel.get('PunterReferenceNumber'),
    }


def parse_order_update(update):
    return {
        'order_id': update.get('BetId'),
        'return_code': update.get('ReturnCode'),
    }


def parse_orders_receipt(order):
    return {
        'order_id': order.get('OrderHandle'),
        'side': Polarity(int(order.get('Polarity'))).name if order.get('Polarity') else None,
        'size_remaining': order.get('UnmatchedStake'),
        'matched_price': order.get('MatchedPrice'),
        'matched_size': order.get('MatchedStake'),
        'matched_lay_size': order.get('MatchedAgainstStake'),
        'sent_time': make_tz_naive(order.get('IssuedAt')),
        'status': OrderStatus(int(order.get('Status'))) if order.get('Status') else None,
        'runner_sequence_number': order.get('SequenceNumber'),
        'runner_id': order.get('SelectionId'),
        'customer_reference': order.get('PunterReferenceNumber'),
        'return_code': order.get('ReturnCode'),
    }


def parse_orders(order):
    return {
        'order_id': order.get('Id'),
        'commission_information': {
                'gross_settlement_amount': order.get('OrderCommissionInformation', {}).get('GrossSettlementAmount'),
                'commission': order.get('OrderCommissionInformation', {}).get('OrderCommission'),
        } if order.get('OrderCommissionInformation') else {},
        'runner_id': order.get('SelectionId'),
        'market_id': order.get('MarketId'),
        'sequence_number': order.get('SequenceNumber'),
        'status': OrderStatus(int(order.get('Status'))).name if order.get('Status') else None,
        'side': Polarity(int(order.get('Polarity'))).name if order.get('Polarity') else None,
        'sent_time': make_tz_naive(order.get('IssuedAt')),
        'price': order.get('RequestedPrice'),
        'remaining_size': order.get('UnmatchedStake'),
        'average_price': order.get('AveragePrice'),
        'matched_price': order.get('MatchedPrice'),
        'matched_size': order.get('MatchedStake'),
        'matched_lay_size': order.get('MatchedAgainstStake'),
        'back_take_size': order.get('TotalForSideTakeStake '),
        'back_make_size': order.get('TotalForSideMakeStake '),
        'customer_reference': order.get('PunterReferenceNumber'),
        'withdrawal_sequence_number': order.get('ExpectedWithdrawalSequenceNumber'),
        'runner_reset_count': order.get('ExpectedSelectionResetCount'),
        'in_play': order.get('IsCurrentlyInRunning'),
        'order_fill_type': OrderKillType(int(order.get('OrderFillType'))).name if order.get('OrderFillType') else None,
        'fill_or_kill_threshold': order.get('FillOrKillThreshold'),
        'cancel_on_in_running': order.get('CancelOnInRunning'),
        'cancel_if_selection_reset': order.get('CancelIfSelectionReset'),
        'commission_base_rate': order.get('PunterCommissionBasis'),
        'commission_take_rate': order.get('TakeCommissionRate'),
        'commission_make_rate': order.get('MakeCommissionRate'),
        }


def parse_single_order(order):
    return {
        'order_id': order.get('Id'),
        'settlement_information': {
                'gross_settlement_amount': order.get('OrderCommissionInformation', {}).get('GrossSettlementAmount')
                if order.get('OrderCommissionInformation') else None,
                'order_commission': order.get('OrderCommissionInformation', {}).get('OrderCommission')
                if order.get('OrderCommissionInformation') else None,
                'market_commission': order.get('OrderCommissionInformation', {}).get('MarketCommission')
                if order.get('OrderCommissionInformation') else None,
                'settlement_time': make_tz_naive(order.get('OrderCommissionInformation', {}).get('MarketSettledDate'))
                if order.get('OrderCommissionInformation') else None,
        },
        'audit_log': [{'timestamp': make_tz_naive(log.get('Time')),
                       'matched_size': log.get('MatchedOrderInformation', {}).get('MatchedStake')
                       if log.get('MatchedOrderInformation') else None,
                       'matched_lay_size': log.get('MatchedOrderInformation', {}).get('MatchedAgainstStake')
                       if log.get('MatchedOrderInformation') else None,
                       'matched_price': log.get('MatchedOrderInformation', {}).get('PriceMatched')
                       if log.get('MatchedOrderInformation') else None,
                       'matched_order_id': log.get('MatchedOrderInformation', {}).get('MatchedOrderID')
                       if log.get('MatchedOrderInformation')else None,
                       'maker': log.get('MatchedOrderInformation', {}).get('WasMake')
                       if log.get('MatchedOrderInformation') else None,
                       'order_commission': log.get('CommissionInformation', {}).get('OrderCommission'),
                       'gross_settlement_amount': log.get('CommissionInformation', {}).get('GrossSettlementAmount'),
                       'order_action': OrderActionType(int(log.get('OrderActionType'))).name,
                       'requested_size': log.get('RequestedStake'),
                       'total_size': log.get('TotalStake'),
                       'total_lay_size': log.get('TotalAgainstStake'),
                       'requested_price': log.get('RequestedPrice'),
                       'average_price': log.get('AveragePrice'),
                       } for log in order.get('AuditLog', {}).get('AuditLog', [])],
        'runner_id': order.get('SelectionId'),
        'market_id': order.get('MarketId'),
        'status': OrderStatus(int(order.get('OrderStatus'))).name if order.get('OrderStatus') else None,
        'in_play': order.get('IsCurrentlyInRunning'),
        'market_status': MarketStatus(int(order.get('MarketStatus'))).name if order.get('MarketStatus') else None,
        'sent_time': make_tz_naive(order.get('IssuedAt')),
        'last_update_time': make_tz_naive(order.get('LastChangedAt')),
        'expiry_time': make_tz_naive(order.get('ExpiresAt')),
        'valid_from': make_tz_naive(order.get('ValidFrom')),
        'order_fill_type': OrderKillType(int(order.get('OrderFillType'))).name if order.get('OrderFillType') else None,
        'fill_or_kill_threshold': order.get('FillOrKillThreshold'),
        'requested_size': order.get('RequestedStake'),
        'requested_price': order.get('RequestedPrice'),
        'expected_selection_reset_count': order.get('ExpectedSelectionResetCount'),
        'total_size': order.get('TotalStake'),
        'remaining_size': order.get('UnmatchedStake'),
        'matched_size': order.get('MatchedStake'),
        'matched_lay_stake': order.get('MatchedAgainstStake'),
        'matched_price': order.get('MatchedPrice'),
        'average_price': order.get('AveragePrice'),
        'matching_time': make_tz_naive(order.get('MatchingTimeStamp')),
        'side': Polarity(int(order.get('Polarity'))) if order.get('Polarity') else None,
        'withdrawal_reprice_option': order.get('WithdrawalRepriceOption'),
        'cancel_on_in_running': order.get('CancelOnInRunning'),
        'cancel_if_selection_reset': order.get('CancelIfSelectionReset'),
        'sequence_number': order.get('SequenceNumber'),
        'customer_reference': order.get('PunterReferenceNumber'),
        'market_type': order.get('MarketType'),
        'expected_withdrawal_sequence_number': order.get('ExpectedWithdrawalSequenceNumber'),
        }
