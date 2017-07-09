

from betdaq.resources.baseresources import BaseResource


class BlacklistInfo(BaseResource):
    class Meta(BaseResource.Meta):
        identifier = 'ApiNamesAndTimes'
        attributes = {
            'ApiName': 'ApiName',
            'RemainingMS': 'RemainingMS',
        }


class Pulse(BaseResource):
    class Meta(BaseResource.Meta):
        identifier = ''
        attributes = {
            'PerformedAt': 'PerformedAt',
            'HeartbeatAction': 'HeartbeatAction',
        }
        datetime_attributes = (
            'PerformedAt'
        )
