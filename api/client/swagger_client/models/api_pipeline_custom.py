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

from swagger_client.models.api_pipeline_dag import ApiPipelineDAG  # noqa: F401,E501
from swagger_client.models.api_pipeline_inputs import (  # noqa: F401
    ApiPipelineInputs,
)


class ApiPipelineCustom(object):
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
        "dag": "ApiPipelineDAG",
        "inputs": "ApiPipelineInputs",
        "name": "str",
        "description": "str",
    }

    attribute_map = {
        "dag": "dag",
        "inputs": "inputs",
        "name": "name",
        "description": "description",
    }

    def __init__(
        self, dag=None, inputs=None, name=None, description=None
    ):  # noqa: E501
        """ApiPipelineCustom - a model defined in Swagger"""  # noqa: E501

        self._dag = None
        self._inputs = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.dag = dag
        if inputs is not None:
            self.inputs = inputs
        self.name = name
        if description is not None:
            self.description = description

    @property
    def dag(self):
        """Gets the dag of this ApiPipelineCustom.  # noqa: E501


        :return: The dag of this ApiPipelineCustom.  # noqa: E501
        :rtype: ApiPipelineDAG
        """
        return self._dag

    @dag.setter
    def dag(self, dag):
        """Sets the dag of this ApiPipelineCustom.


        :param dag: The dag of this ApiPipelineCustom.  # noqa: E501
        :type: ApiPipelineDAG
        """
        if dag is None:
            raise ValueError(
                "Invalid value for `dag`, must not be `None`"
            )

        self._dag = dag

    @property
    def inputs(self):
        """Gets the inputs of this ApiPipelineCustom.  # noqa: E501


        :return: The inputs of this ApiPipelineCustom.  # noqa: E501
        :rtype: ApiPipelineInputs
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ApiPipelineCustom.


        :param inputs: The inputs of this ApiPipelineCustom.  # noqa: E501
        :type: ApiPipelineInputs
        """

        self._inputs = inputs

    @property
    def name(self):
        """Gets the name of this ApiPipelineCustom.  # noqa: E501

        Name of the custom pipeline  # noqa: E501

        :return: The name of this ApiPipelineCustom.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiPipelineCustom.

        Name of the custom pipeline  # noqa: E501

        :param name: The name of this ApiPipelineCustom.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApiPipelineCustom.  # noqa: E501

        Optional description of the custom pipeline  # noqa: E501

        :return: The description of this ApiPipelineCustom.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiPipelineCustom.

        Optional description of the custom pipeline  # noqa: E501

        :param description: The description of this ApiPipelineCustom.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(ApiPipelineCustom, dict):
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
        if not isinstance(other, ApiPipelineCustom):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
