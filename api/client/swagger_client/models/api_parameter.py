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

from swagger_client.models.any_value import AnyValue  # noqa: F401,E501


class ApiParameter(object):
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
        "name": "str",
        "description": "str",
        "default": "AnyValue",
        "value": "AnyValue",
    }

    attribute_map = {
        "name": "name",
        "description": "description",
        "default": "default",
        "value": "value",
    }

    def __init__(
        self, name=None, description=None, default=None, value=None
    ):  # noqa: E501
        """ApiParameter - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._default = None
        self._value = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if default is not None:
            self.default = default
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this ApiParameter.  # noqa: E501


        :return: The name of this ApiParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiParameter.


        :param name: The name of this ApiParameter.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApiParameter.  # noqa: E501


        :return: The description of this ApiParameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiParameter.


        :param description: The description of this ApiParameter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def default(self):
        """Gets the default of this ApiParameter.  # noqa: E501


        :return: The default of this ApiParameter.  # noqa: E501
        :rtype: AnyValue
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this ApiParameter.


        :param default: The default of this ApiParameter.  # noqa: E501
        :type: AnyValue
        """

        self._default = default

    @property
    def value(self):
        """Gets the value of this ApiParameter.  # noqa: E501


        :return: The value of this ApiParameter.  # noqa: E501
        :rtype: AnyValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ApiParameter.


        :param value: The value of this ApiParameter.  # noqa: E501
        :type: AnyValue
        """

        self._value = value

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
        if issubclass(ApiParameter, dict):
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
        if not isinstance(other, ApiParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
