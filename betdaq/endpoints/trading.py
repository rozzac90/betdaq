
import datetime

from betdaq.enums import HeartbeatAction
from betdaq.utils import clean_locals
from betdaq.endpoints.baseendpoint import BaseEndpoint


class Trading(BaseEndpoint):

    def list_blacklist_information(self):
        """
        Lists the black-list status for the punter.
        
        :return: list of every API from which the Punter is currentltly black-listed along with the remaining time 
                 (in milli-seconds) of the black-list period for that API. 
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('ListBlacklistInformation', {}, secure=True)
        return self.process_response(response, date_time_sent, 'ApiNamesAndTimes')

    def suspend_from_trading(self):
        """
        Suspend any of your orders from being matched. For emergency use only.
        
        :return: response of request success.
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('SuspendFromTrading', {}, secure=True)
        return self.process_response(response, date_time_sent, None)

    def unsuspend_from_trading(self):
        """
        Reverse the suspension of trading. All active orders must be cancelled or suspended before you can unsuspend.

        :return: response of request success.
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('UnsuspendFromTrading', {}, secure=True)
        return self.process_response(response, date_time_sent, None)

    def register_heartbeat(self, HeartbeatAction=HeartbeatAction.CancelOrders.value, ThresholdMs=6000):
        """
        Register the Punter as requiring a Heartbeat. Must send a Pulse < every ThresholdMs to stay alive.
        
        :param HeartbeatAction: The action that should be taken if a Pulse is not received within the threshold. 
        :type HeartbeatAction: betdaq_py.enums.HeartbeatAction
        :param ThresholdMs: The maximum period (in milli-seconds) that can elapse between Pulse API calls being 
                            received before the system takes the relevant action. 
        :return: response of request success.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('RegisterHeartbeat', params, secure=True)
        return self.process_response(response, date_time_sent, None)

    def deregister_heartbeat(self):
        """
        Deregister the Punter as requiring a Heartbeat.

        :return: response of request success.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('DeregisterHeartbeat', params, secure=True)
        return self.process_response(response, date_time_sent, None)

    def change_hearbeat(self, HeartbeatAction=HeartbeatAction.CancelOrders.value, ThresholdMs=6000):
        """
        Update the parameter of Heartbeat.

        :param HeartbeatAction: The action that should be taken if a Pulse is not received within the threshold. 
        :type HeartbeatAction: betdaq_py.enums.HeartbeatAction
        :param ThresholdMs: The maximum period (in milli-seconds) that can elapse between Pulse API calls being 
                            received before the system takes the relevant action. 
        :return: response of request success.
        """
        params = clean_locals(locals())
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('ChangeHeartbeatRegistration', params, secure=True)
        return self.process_response(response, date_time_sent, None)

    def send_pulse(self):
        """
        Notify the system that the application is still active and still has connectivity.
        
        :return: Time of pulse performance.
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('Pulse', {}, secure=True)
        return self.process_response(response, date_time_sent, None)
