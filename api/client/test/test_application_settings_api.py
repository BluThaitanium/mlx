# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0
# coding: utf-8

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client  # noqa: F401
from swagger_client.api.application_settings_api import (  # noqa: F401
    ApplicationSettingsApi,
)
from swagger_client.rest import ApiException  # noqa: F401


class TestApplicationSettingsApi(unittest.TestCase):
    """ApplicationSettingsApi unit test stubs"""

    def setUp(self):
        self.api = (
            swagger_client.api.application_settings_api.ApplicationSettingsApi()
        )

    def tearDown(self):
        pass

    def test_get_application_settings(self):
        """Test case for get_application_settings"""
        pass

    def test_modify_application_settings(self):
        """Test case for modify_application_settings"""
        pass

    def test_set_application_settings(self):
        """Test case for set_application_settings"""
        pass


if __name__ == "__main__":
    unittest.main()
