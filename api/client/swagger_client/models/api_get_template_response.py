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


class ApiGetTemplateResponse(object):
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
    swagger_types = {"template": "str", "url": "str"}

    attribute_map = {"template": "template", "url": "url"}

    def __init__(self, template=None, url=None):  # noqa: E501
        """ApiGetTemplateResponse - a model defined in Swagger"""  # noqa: E501

        self._template = None
        self._url = None
        self.discriminator = None

        if template is not None:
            self.template = template
        if url is not None:
            self.url = url

    @property
    def template(self):
        """Gets the template of this ApiGetTemplateResponse.  # noqa: E501

        The YAML template file content  # noqa: E501

        :return: The template of this ApiGetTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ApiGetTemplateResponse.

        The YAML template file content  # noqa: E501

        :param template: The template of this ApiGetTemplateResponse.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def url(self):
        """Gets the url of this ApiGetTemplateResponse.  # noqa: E501

        The URL to download the template text from S3 storage (Minio)

        :return: The url of this ApiGetTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ApiGetTemplateResponse.

        The URL to download the template text from S3 storage (Minio)

        :param url: The url of this ApiGetTemplateResponse.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(ApiGetTemplateResponse, dict):
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
        if not isinstance(other, ApiGetTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
