# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0
# coding: utf-8

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.30-upload-catalog-from-url
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint  # noqa: F401
import re  # noqa: F401

import six  # noqa: F401


class ApiCatalogUpload(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "api_access_tokens": "list[ApiAccessToken]",
        "components": "list[ApiCatalogUploadItem]",
        "datasets": "list[ApiCatalogUploadItem]",
        "models": "list[ApiCatalogUploadItem]",
        "notebooks": "list[ApiCatalogUploadItem]",
        "pipelines": "list[ApiCatalogUploadItem]",
    }

    attribute_map = {
        "api_access_tokens": "api_access_tokens",
        "components": "components",
        "datasets": "datasets",
        "models": "models",
        "notebooks": "notebooks",
        "pipelines": "pipelines",
    }

    def __init__(
        self,
        api_access_tokens=None,
        components=None,
        datasets=None,
        models=None,
        notebooks=None,
        pipelines=None,
    ):  # noqa: E501
        """ApiCatalogUpload - a model defined in Swagger"""  # noqa: E501

        self._api_access_tokens = None
        self._components = None
        self._datasets = None
        self._models = None
        self._notebooks = None
        self._pipelines = None
        self.discriminator = None

        if api_access_tokens is not None:
            self.api_access_tokens = api_access_tokens
        if components is not None:
            self.components = components
        if datasets is not None:
            self.datasets = datasets
        if models is not None:
            self.models = models
        if notebooks is not None:
            self.notebooks = notebooks
        if pipelines is not None:
            self.pipelines = pipelines

    @property
    def api_access_tokens(self):
        """Gets the api_access_tokens of this ApiCatalogUpload.  # noqa: E501

        A mapping of read-only API access tokens to a partial URL.  # noqa: E501

        :return: The api_access_tokens of this ApiCatalogUpload.  # noqa: E501
        :rtype: list[ApiAccessToken]
        """
        return self._api_access_tokens

    @api_access_tokens.setter
    def api_access_tokens(self, api_access_tokens):
        """Sets the api_access_tokens of this ApiCatalogUpload.

        A mapping of read-only API access tokens to a partial URL.  # noqa: E501

        :param api_access_tokens: The api_access_tokens of this ApiCatalogUpload.  # noqa: E501
        :type: list[ApiAccessToken]
        """

        self._api_access_tokens = api_access_tokens

    @property
    def components(self):
        """Gets the components of this ApiCatalogUpload.  # noqa: E501


        :return: The components of this ApiCatalogUpload.  # noqa: E501
        :rtype: list[ApiCatalogUploadItem]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this ApiCatalogUpload.


        :param components: The components of this ApiCatalogUpload.  # noqa: E501
        :type: list[ApiCatalogUploadItem]
        """

        self._components = components

    @property
    def datasets(self):
        """Gets the datasets of this ApiCatalogUpload.  # noqa: E501


        :return: The datasets of this ApiCatalogUpload.  # noqa: E501
        :rtype: list[ApiCatalogUploadItem]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this ApiCatalogUpload.


        :param datasets: The datasets of this ApiCatalogUpload.  # noqa: E501
        :type: list[ApiCatalogUploadItem]
        """

        self._datasets = datasets

    @property
    def models(self):
        """Gets the models of this ApiCatalogUpload.  # noqa: E501


        :return: The models of this ApiCatalogUpload.  # noqa: E501
        :rtype: list[ApiCatalogUploadItem]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this ApiCatalogUpload.


        :param models: The models of this ApiCatalogUpload.  # noqa: E501
        :type: list[ApiCatalogUploadItem]
        """

        self._models = models

    @property
    def notebooks(self):
        """Gets the notebooks of this ApiCatalogUpload.  # noqa: E501


        :return: The notebooks of this ApiCatalogUpload.  # noqa: E501
        :rtype: list[ApiCatalogUploadItem]
        """
        return self._notebooks

    @notebooks.setter
    def notebooks(self, notebooks):
        """Sets the notebooks of this ApiCatalogUpload.


        :param notebooks: The notebooks of this ApiCatalogUpload.  # noqa: E501
        :type: list[ApiCatalogUploadItem]
        """

        self._notebooks = notebooks

    @property
    def pipelines(self):
        """Gets the pipelines of this ApiCatalogUpload.  # noqa: E501


        :return: The pipelines of this ApiCatalogUpload.  # noqa: E501
        :rtype: list[ApiCatalogUploadItem]
        """
        return self._pipelines

    @pipelines.setter
    def pipelines(self, pipelines):
        """Sets the pipelines of this ApiCatalogUpload.


        :param pipelines: The pipelines of this ApiCatalogUpload.  # noqa: E501
        :type: list[ApiCatalogUploadItem]
        """

        self._pipelines = pipelines

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(ApiCatalogUpload, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiCatalogUpload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
