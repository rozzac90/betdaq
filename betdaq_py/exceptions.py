
from enum import Enum

class BetdaqError(Exception):
    """Base class for Betdaq Errors"""
    pass


class APIError(BetdaqError):
    """Exception raised if error is found"""

    def __init__(self, response, method=None, params=None, exception=None):
        if response:
            error_data = response.get('ResponseStatus', {})
            message = '%s \nParams: %s \nException: %s \nErrorCode: %s \nError Detail: %s' % (
                method, params, exception, error_data.get('Code'), response.get('ExtraInformation')
            )
        else:
            message = '%s \nParams: %s \nException: %s' % (
                method, params, exception
            )
        super(APIError, self).__init__(message)


class ResourceError(BetdaqError):
    def __init__(self):
        message = 'The API call was not processed successfully because of some critical resource constraint.' \
                  'This exception was as a result of a serious resource constraint within the exchange.'
        super(ResourceError, self).__init__(message)


class BetdaqSystemError(BetdaqError):
    def __init__(self):
        message = 'The API call was not processed successfully because of some serious technical error within the system.'
        super(BetdaqSystemError, self).__init__(message)


class EventClassifierDoesNotExist(BetdaqError):
    def __init__(self, event):
        message = 'An Event Classifier with the handle %s does not exist.' % event
        super(EventClassifierDoesNotExist, self).__init__(message)


class MarketDoesNotExist(BetdaqError):
    def __init__(self, market):
        message = 'A Market with the handle %s does not exist.' % market
        super(MarketDoesNotExist, self).__init__(message)


class SelectionDoesNotExist(BetdaqError):
    def __init__(self, selection):
        message = 'A selection with the handle %s does not exist.' % selection
        super(SelectionDoesNotExist, self).__init__(message)


class MarketNotActive(BetdaqError):
    def __init__(self, market):
        message = 'The action requested cannot be performed because the Market %s is not active.' % market
        super(MarketNotActive, self).__init__(message)


class MarketNeitherSuspendedNorActive(BetdaqError):
    def __init__(self, market):
        message = 'The action requested cannot be performed because the Market %s is not active or suspended.' % market
        super(MarketNeitherSuspendedNorActive, self).__init__(message)


class SelectionNotActive(BetdaqError):
    def __init__(self, selection):
        message = 'The action requested cannot be performed because the selection %s is not active or suspended.' % selection
        super(SelectionNotActive, self).__init__(message)


class InsufficientVirtualPunterFunds(BetdaqError):
    def __init__(self):
        message = 'The Order specified could not be placed because the increase in the amount of the Virtual ' \
                  'Punter’s funds that would need to be frozen as a result of that Order is greater than the ' \
                  "value specified for ‘maxVirtualReservationIncrease’"
        super(InsufficientVirtualPunterFunds, self).__init__(message)


class OrderDoesNotExist(BetdaqError):
    def __init__(self, order_id):
        message = 'An Order with the handle %s does not exist.' % order_id
        super(OrderDoesNotExist, self).__init__(message)


class NoUnmatchedAmount(BetdaqError):
    def __init__(self, order_id):
        message = 'The Order {} could not be placed, cancelled or changed because the amount ' \
                  'requested is negative or the entire stake of the Order has already been matched.'.format(order_id)
        super(NoUnmatchedAmount, self).__init__(message)


class ResetHasOccurred(BetdaqError):
    def __init__(self, order_id):
        message = 'The order was not placed because the expectedSelectionResetCount {} on the Order does not match ' \
                  'the current selectionResetCount for the Selection.'.format(order_id)
        super(ResetHasOccurred, self).__init__(message)


class OrderAlreadySuspended(BetdaqError):
    def __init__(self, order_id):
        message = 'The order %s is already suspended' % order_id
        super(OrderAlreadySuspended, self).__init__(message)


class TradingCurrentlySuspended(BetdaqError):
    def __init__(self, order_id):
        message = 'The order %s could not be processed because all trading is currently suspended on the Exchange.' % order_id
        super(TradingCurrentlySuspended, self).__init__(message)


class InvalidOdds(BetdaqError):
    def __init__(self, odds, stake):
        message = 'The odds %s or stake %s are not valid.' % (odds, stake)
        super(InvalidOdds, self).__init__(message)


class WithdrawalSequenceNumberIsInvalid(BetdaqError):
    def __init__(self, sequenceNumber):
        message = 'The Order was not placed because the withdrawal sequence number %s is greater than the current' \
                  ' withdrawal sequence number for the market.' % sequenceNumber
        super(WithdrawalSequenceNumberIsInvalid, self).__init__(message)


class MaximumInputRecordsExceeded(BetdaqError):
    def __init__(self):
        message = 'Exceeded the limit on the number of parameters that can be specified.'
        super(MaximumInputRecordsExceeded, self).__init__(message)


class PunterSuspended(BetdaqError):
    def __init__(self):
        message = 'User is currently suspended.'
        super(PunterSuspended, self).__init__(message)


class PunterProhibitedFromPlacingOrders(BetdaqError):
    def __init__(self):
        message = 'Punter is prohibited from placing orders on exchange.'
        super(PunterProhibitedFromPlacingOrders, self).__init__(message)


class InsufficientPunterFunds(BetdaqError):
    def __init__(self):
        message = 'Punter does not have sufficient unfrozen funds.'
        super(InsufficientPunterFunds, self).__init__(message)


class OrderAPIInProgress(BetdaqError):
    def __init__(self):
        message = 'Another order API is currently in progress for this Punter. A Punter can not issue more ' \
                  'than one order API (PlaceSimgleOrder, PlaceGroupOrder or ChangeOrder) at the same time.'
        super(OrderAPIInProgress, self).__init__(message)


class PunterOrderMismatch(BetdaqError):
    def __init__(self):
        message = 'One or more of the Orders specified were not issued by the Punter specified or there is a ' \
                  'mis-match between the Punter implied and the object specified.'
        super(PunterOrderMismatch, self).__init__(message)


class MarketNotEnabledForMultiples(BetdaqError):
    def __init__(self):
        message = 'The market of one or more selections does not support multiple bets.	'
        super(MarketNotEnabledForMultiples, self).__init__(message)


class MultipleLayerParameterAlreadyExists(BetdaqError):
    def __init__(self):
        message = 'A MultiplePriceMultipler for the MultipleLayer with the numberOfSelections specified already exists.'
        super(MultipleLayerParameterAlreadyExists, self).__init__(message)


class LevelsRequestedExceedsMaximum(BetdaqError):
    def __init__(self):
        message = 'The number of levels of combination requested exceeds the system defined maximum'
        super(LevelsRequestedExceedsMaximum, self).__init__(message)


class NoMultipleOfferAvailable(BetdaqError):
    def __init__(self):
        message = 'The requested multiple bet was not matched because there was no multiple offers available.'
        super(NoMultipleOfferAvailable, self).__init__(message)


class InRunningDelayInEffect(BetdaqError):
    def __init__(self):
        message = 'An attempt was made to change an order that is currently subject to an in-running delay.'
        super(InRunningDelayInEffect, self).__init__(message)


class MultipleSelectionsUnderSameEvent(BetdaqError):
    def __init__(self):
        message = 'An attempt was made to place a multiple bet that contained two or more ' \
                  'Selections belonging to markets under the same event classifier'
        super(MultipleSelectionsUnderSameEvent, self).__init__(message)


class MultipleSelectionsWithSameName(BetdaqError):
    def __init__(self):
        message = 'An attempt was made to place a multiple bet that contained two or more selections ' \
                  'with exactly the same name.'
        super(MultipleSelectionsWithSameName, self).__init__(message)


class DuplicateOrderSpecified(BetdaqError):
    def __init__(self):
        message = 'The same order was specified more than once in the same API call.'
        super(DuplicateOrderSpecified, self).__init__(message)


class OrderNotSuspended(BetdaqError):
    def __init__(self):
        message = 'The order is not currently suspended.'
        super(OrderNotSuspended, self).__init__(message)


class PunterIsSuspendedFromTrading(BetdaqError):
    def __init__(self):
        message = 'Punter concerned is currently suspended from trading.'
        super(PunterIsSuspendedFromTrading, self).__init__(message)


class PunterHasActiveOrders(BetdaqError):
    def __init__(self):
        message = 'An attempt was made to unsuspend Punter from trading. A Punter can only be ' \
                  'unsuspended if the Punter currently has no active orders. ' \
                  'However the Punter concerned currently does have active orders.'
        super(PunterHasActiveOrders, self).__init__(message)


class PunterNotSuspendedFromTrading(BetdaqError):
    def __init__(self):
        message = 'The requested operation could not be completed because the Punter concerned is not currently suspended from trading'
        super(PunterNotSuspendedFromTrading, self).__init__(message)


class ExpiryTimeInThePast(BetdaqError):
    def __init__(self):
        message = 'The requested operation could not be performed because the expiry time specified is in the past'
        super(ExpiryTimeInThePast, self).__init__(message)


class NoChangeSpecified(BetdaqError):
    def __init__(self):
        message = 'Change order could not be performed because the price specified is the current price of the order concerned'
        super(NoChangeSpecified, self).__init__(message)


class SoapHeaderNotSupplied(BetdaqError):
    def __init__(self):
        message = 'The SOAP header was not specified. All External API calls must include a SOAP header.'
        super(SoapHeaderNotSupplied, self).__init__(message)


class IncorrectVersionNumber(BetdaqError):
    def __init__(self):
        message = 'An incorrect version number specified in API header.'
        super(IncorrectVersionNumber, self).__init__(message)


class NoUsernameSpecified(BetdaqError):
    def __init__(self):
        message = 'You must specify your username in the API header.'
        super(NoUsernameSpecified, self).__init__(message)


class InvalidParameters(BetdaqError):
    def __init__(self):
        message = 'Invalid parameters were passed to the web method.'
        super(InvalidParameters, self).__init__(message)


class NoPasswordSpecified(BetdaqError):
    def __init__(self):
        message = 'You must specify your password in the API header.'
        super(NoPasswordSpecified, self).__init__(message)


class MultipleCombinationExclusionAlreadyExists(BetdaqError):
    def __init__(self):
        message = 'There is currently an active MultipleCombinationExclusion with the set of Selections specified.'
        super(MultipleCombinationExclusionAlreadyExists, self).__init__(message)


class MultipleCombinationExlcusionDoesNotExist(BetdaqError):
    def __init__(self):
        message = 'There is not currently an active MultipleCombinationExclusion with the set of Selections specified ' \
                  'for the multiple layer specified.'
        super(MultipleCombinationExlcusionDoesNotExist, self).__init__(message)


class InvalidPassword(BetdaqError):
    def __init__(self):
        message = 'The password specified is not a valid password. Specifically it does not conform to the rules ' \
                  'defined for such passwords.'
        super(InvalidPassword, self).__init__(message)


class PunterIsBlacklisted(BetdaqError):
    def __init__(self):
        message = 'The operation requested was not executed because the Punter concerned is currently ' \
                  'black-listed from performing that action.'
        super(PunterIsBlacklisted, self).__init__(message)


class PunterNotRegisteredAsMultipleLayer(BetdaqError):
    def __init__(self):
        message = 'The requested action could not be performed because the Punter concerned has not been ' \
                  'registered as a multiple layer.'
        super(PunterNotRegisteredAsMultipleLayer, self).__init__(message)


class PunterAlreadyRegisteredForHeartbeat(BetdaqError):
    def __init__(self):
        message = 'The operation could not complete because the Punter concerned is already registered for a Heartbeat.'
        super(PunterAlreadyRegisteredForHeartbeat, self).__init__(message)


class PunterNotRegisteredForHeartbeat(BetdaqError):
    def __init__(self):
        message = 'The operation could not complete because the Punter concerened is not registered for a Heartbeat.'
        super(PunterNotRegisteredForHeartbeat, self).__init__(message)


class ThresholdSpecifiedTooSmall(BetdaqError):
    def __init__(self):
        message = 'The threshold value specified is less than the system defined minimum threshold value.'
        super(ThresholdSpecifiedTooSmall, self).__init__(message)


class UnmatchedOrderCouldResult(BetdaqError):
    def __init__(self):
        message = 'The attempt to place an order was not successful because it could result in an unmatched order ' \
                  'remaining on the system. The specific API call used can only be used for orders that can not result' \
                  ' in a an unmatched order. For example, you can not specify a KillType of FillOrKillDontCancel.'
        super(UnmatchedOrderCouldResult, self).__init__(message)


class PunterNotAuthorisedForAPI(BetdaqError):
    def __init__(self):
        message = 'The punter concerned is not authorised to use the external API.'
        super(PunterNotAuthorisedForAPI, self).__init__(message)


class MarketIsForRealMoney(BetdaqError):
    def __init__(self):
        message = 'The requested operation cannot be performed because the market concerned is not a play market ' \
                  'but the currency specified is a play currency.'
        super(MarketIsForRealMoney, self).__init__(message)


class MarketIsForPlayMoney(BetdaqError):
    def __init__(self):
        message = 'The requested operation cannot be performed because the market concerned is a plat market ' \
                  'but the currency specified is a real currency.'
        super(MarketIsForPlayMoney, self).__init__(message)


class CannotChangeToSPIfUnmatched(BetdaqError):
    def __init__(self):
        message = 'The requested operation could not be performed because the orderFillType of the order ' \
                  'concerned is not Normal.'
        super(CannotChangeToSPIfUnmatched, self).__init__(message)


class InvalidUsername(BetdaqError):
    def __init__(self):
        message = 'Username provided is not valid.'
        super(InvalidUsername, self).__init__(message)
