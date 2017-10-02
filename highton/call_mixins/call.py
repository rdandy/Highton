from abc import ABCMeta

import requests
from requests.auth import HTTPBasicAuth

from highton.highton_constants import HightonConstants
from highton.highton_settings import USERNAME, API_KEY


class Call(metaclass=ABCMeta):
    ENDPOINT = None

    @classmethod
    def _request(cls, method, endpoint=None, params=None, data=None):
        return requests.request(
            method=method,
            url='https://{user}.{highrise_url}/{endpoint}.xml'.format(
                user=USERNAME,
                highrise_url=HightonConstants.HIGHRISE_URL,
                endpoint=endpoint if endpoint else cls.ENDPOINT
            ),
            headers={'Content-Type': 'application/xml'},
            auth=HTTPBasicAuth(username=API_KEY, password=''),
            params=params,
            data=data,
        )

    @classmethod
    def _get_request(cls, endpoint=None, params=None):
        return cls._request(method=HightonConstants.GET, endpoint=endpoint, params=params)

    @classmethod
    def _post_request(cls, data, endpoint=None, params=None):
        return cls._request(method=HightonConstants.POST, endpoint=endpoint, params=params, data=data)

    @classmethod
    def _put_request(cls, data, endpoint=None, params=None):
        return cls._request(method=HightonConstants.PUT, endpoint=endpoint, params=params, data=data)

    @classmethod
    def _delete_request(cls, endpoint=None, params=None):
        return cls._request(method=HightonConstants.DELETE, endpoint=endpoint, params=params)
