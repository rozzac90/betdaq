
import datetime

from betdaq.utils import clean_locals
from betdaq.endpoints.baseendpoint import BaseEndpoint
from betdaq.resources.accountresources import parse_account_balance, parse_account_postings


class Account(BaseEndpoint):

    def get_account_balances(self):
        """
        Get summary of current balances.

        :return: account information for logged in user.
        :rtype: dict
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('GetAccountBalances', params, secure=True)
        data = self.process_response(response, date_time_sent, None)
        return parse_account_balance(data.get('data', {})) if data.get('data') else {}

    def get_account_transactions(self, StartTime, EndTime):
        """
        Get account transactions between two given date and times.

        :param StartTime: earlier time to include transactions from.
        :type StartTime: Timestamp
        :param EndTime: latest time to include transactions until.
        :type EndTime: Timestamp
        :return: account transactions over the specified period.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('ListAccountPostings', params, secure=True)
        data = self.process_response(response, date_time_sent, None)
        return parse_account_postings(data.get('data', {})) if data.get('data') else {}

    def get_account_transactions_by_id(self, TransactionId):
        """
        Get account transactions with transactionId greater than that specified.

        :param TransactionId: lower cutoff for transactionIds to include.
        :type TransactionId: int
        :return: account transactions greater than specified transactionId.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('ListAccountPostingsById', params, secure=True)
        data = self.process_response(response, date_time_sent, None)
        return parse_account_postings(data.get('data', {})) if data.get('data') else {}

    def change_account_password(self, Password):
        """
        Change the password for the logged in user.

        :param Password: new password to be used for logged in user.
        :type Password: str
        :return: None
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('ChangePassword', params, secure=True)
        data = self.process_response(response, date_time_sent, None)
        return data.get('data', {})
