
import datetime
from requests import ConnectionError
from zeep.helpers import serialize_object

from betdaq_py.exceptions import APIError
from betdaq_py.utils import check_status_code, make_tz_naive, listy_mc_list


class BaseEndpoint(object):

    def __init__(self, parent):
        """
        :param parent: API client.
        """
        self.client = parent

    def request(self, method, params, secure=False):
        """
        :param method: The endpoint to be requested.
        :param params: Params to be used in request.
        :param secure: Whether the method belongs to the secure or readonly service.
        """
        try:
            if secure:
                response = self.client.secure_client.service[method](params)
            else:
                response = self.client.readonly_client.service[method](params)
        except ConnectionError:
            raise APIError(None, method, params, 'ConnectionError')
        except Exception as e:
            raise APIError(None, method, params, e)
        return serialize_object(response)

    @staticmethod
    def process_response(response, date_time_sent, result_target, error_handler=None):
        """
        :param response: Response from request
        :param date_time_sent: Date time sent
        :param error_handler: function to parse _raw_elements from zeep response.
        :param result_target: name of the key to get response data from, changes per endpoint.
        """
        date_time_received = make_tz_naive(response.get('Timestamp')) or datetime.datetime.utcnow()
        if error_handler and response.get('_raw_elements'):
            response = error_handler(response)
        return {
            'data': response.get(result_target, []) if result_target else response,
            'date_time_sent': date_time_sent,
            'date_time_received': date_time_received,
        }
