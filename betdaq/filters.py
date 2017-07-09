
from betdaq.utils import clean_locals
from betdaq.enums import Boolean, WithdrawRepriceOption, OrderKillType


def create_order(SelectionId, Stake, Price, Polarity, ExpectedSelectionResetCount, ExpectedWithdrawalSequenceNumber,
                 CancelOnInRunning=Boolean.T, CancelIfSelectionReset=Boolean.T, ExpiresAt=None,
                 WithdrawalRepriceOption=WithdrawRepriceOption.Cancel, KillType=OrderKillType.FillOrKillDontCancel,
                 FillOrKillThreshold=0.0, PunterReferenceNumber=1):
    """
    Create an order to send to exchange.
    
    :param SelectionId: Id number of the selection on which the order is to be placed
    :type SelectionId: int
    :param Stake: Amount for which the order is to be placed for.
    :type Stake: float
    :param Price: Price at which order is to be placed.
    :type Price: float
    :param Polarity: side on which order is to be placed.
    :type Polarity: betdaq_py.enums.Polarity
    :param ExpectedSelectionResetCount: must match SelectionResetCount value in GetMarketInformation and GetPrices 
                                        to ensure state of the market before placing a bet. If not matching server
                                        bet will not be placed and error is raised.
    :type ExpectedSelectionResetCount: int
    :param ExpectedWithdrawalSequenceNumber: should match withdrawalSequenceNumber value in GetMarketInformation and 
                                             GetPrices. If not matching server then your bet WILL be accepted, but it 
                                             will be repriced.
    :type ExpectedWithdrawalSequenceNumber: int
    :param CancelOnInRunning: Cancel any unmatched orders when the market changes to an in-running market.
    :type CancelOnInRunning: betdaq_py.enums.Boolean
    :param CancelIfSelectionReset: Cancel any unmatched bets if the selection is reset. 
                                   This can occur when the Market is reset (eg a goal is scored).
    :type CancelIfSelectionReset: betdaq_py.enums.Boolean
    :param ExpiresAt: Specify a specific time for an order to expire, times in the past are instantly cancelled.
    :type ExpiresAt: datetime
    :param WithdrawalRepriceOption: Define what to do with the order in case of withdrawal, default to cancel.
    :type WithdrawalRepriceOption: betdaq_py.enums.WithdrawalRepriceOption
    :param KillType: whether to define order as a type of Fill/Kill order, default order will be limit order.
    :type KillType: betdaq_py.enums.OrderKillType
    :param FillOrKillThreshold: Lower limit for order to be partially filled. only required if KillType is 
                                FillOrKill or FillOrKillDontCancel
    :type FillOrKillThreshold: float
    :param PunterReferenceNumber: optional ID provided for customers own reference.
    :type PunterReferenceNumber: int
    :return: dictionary of all order information which can be sent to exchange.
    """
    return clean_locals(locals())


def update_order(BetId, DeltaStake, Price, ExpectedSelectionResetCount, ExpectedWithdrawalSequenceNumber,
                 CancelOnInRunning=None, CancelIfSelectionReset=None, SetToBeSPIfUnmatched=None):
    """
    
    :param BetId: ID of the bet to be updated.
    :type BetId: int
    :param DeltaStake: Amount to change the stake of the bet by.
    :type DeltaStake: float
    :param Price: Price at which to place bet at.
    :param ExpectedSelectionResetCount: must match SelectionResetCount value in GetMarketInformation and GetPrices 
                                        to ensure state of the market before placing a bet. If not matching server
                                        bet will not be placed and error is raised.
    :type ExpectedSelectionResetCount: int
    :param ExpectedWithdrawalSequenceNumber: should match withdrawalSequenceNumber value in GetMarketInformation and 
                                             GetPrices. If not matching server then your bet WILL be accepted, but it 
                                             will be repriced.
    :type ExpectedWithdrawalSequenceNumber: int
    :param CancelOnInRunning: Cancel any unmatched orders when the market changes to an in-running market.
    :type CancelOnInRunning: betdaq_py.enums.Boolean
    :param CancelIfSelectionReset: Cancel any unmatched bets if the selection is reset. 
                                   This can occur when the Market is reset (eg a goal is scored).
    :type CancelIfSelectionReset: betdaq_py.enums.Boolean
    :param SetToBeSPIfUnmatched: whether to set bet to SP when market turns in play if it is unmatched.
    :type SetToBeSPIfUnmatched: betdaq_py.enums.Boolean
    :return: dictionary of the order information to update on exchange.
    """
    return clean_locals(locals())
