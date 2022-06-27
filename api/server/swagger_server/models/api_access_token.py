# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util  # noqa: F401


class ApiAccessToken(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, api_token: str = None, url_host: str = None):  # noqa: E501
        """ApiAccessToken - a model defined in Swagger

        :param api_token: The api_token of this ApiAccessToken.  # noqa: E501
        :type api_token: str
        :param url_host: The url_host of this ApiAccessToken.  # noqa: E501
        :type url_host: str
        """
        self.swagger_types = {"api_token": str, "url_host": str}

        self.attribute_map = {"api_token": "api_token", "url_host": "url_host"}

        self._api_token = api_token
        self._url_host = url_host

    @classmethod
    def from_dict(cls, dikt) -> "ApiAccessToken":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiAccessToken of this ApiAccessToken.  # noqa: E501
        :rtype: ApiAccessToken
        """
        return util.deserialize_model(dikt, cls)

    @property
    def api_token(self) -> str:
        """Gets the api_token of this ApiAccessToken.

        A read-only API access token.  # noqa: E501

        :return: The api_token of this ApiAccessToken.
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token: str):
        """Sets the api_token of this ApiAccessToken.

        A read-only API access token.  # noqa: E501

        :param api_token: The api_token of this ApiAccessToken.
        :type api_token: str
        """
        if api_token is None:
            raise ValueError(
                "Invalid value for `api_token`, must not be `None`"
            )

        self._api_token = api_token

    @property
    def url_host(self) -> str:
        """Gets the url_host of this ApiAccessToken.

        The API server host that this API token applies to.  # noqa: E501

        :return: The url_host of this ApiAccessToken.
        :rtype: str
        """
        return self._url_host

    @url_host.setter
    def url_host(self, url_host: str):
        """Sets the url_host of this ApiAccessToken.

        The API server host that this API token applies to.  # noqa: E501

        :param url_host: The url_host of this ApiAccessToken.
        :type url_host: str
        """
        if url_host is None:
            raise ValueError(
                "Invalid value for `url_host`, must not be `None`"
            )

        self._url_host = url_host
