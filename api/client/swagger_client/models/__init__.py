# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0
# coding: utf-8

# flake8: noqa
"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.30-upload-catalog-from-url
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.any_value import AnyValue
from swagger_client.models.api_access_token import ApiAccessToken
from swagger_client.models.api_asset import ApiAsset
from swagger_client.models.api_catalog_upload import ApiCatalogUpload
from swagger_client.models.api_catalog_upload_item import ApiCatalogUploadItem
from swagger_client.models.api_credential import ApiCredential
from swagger_client.models.api_generate_code_response import ApiGenerateCodeResponse
from swagger_client.models.api_generate_model_code_response import (  # noqa: F401
    ApiGenerateModelCodeResponse,
)
from swagger_client.models.api_get_template_response import ApiGetTemplateResponse
from swagger_client.models.api_inferenceservice import ApiInferenceservice
from swagger_client.models.api_list_catalog_items_response import (  # noqa: F401
    ApiListCatalogItemsResponse,
)
from swagger_client.models.api_list_catalog_upload_errors import (  # noqa: F401
    ApiListCatalogUploadErrors,
)
from swagger_client.models.api_list_components_response import ApiListComponentsResponse
from swagger_client.models.api_list_credentials_response import (  # noqa: F401
    ApiListCredentialsResponse,
)
from swagger_client.models.api_list_datasets_response import ApiListDatasetsResponse
from swagger_client.models.api_list_inferenceservices_response import (  # noqa: F401
    ApiListInferenceservicesResponse,
)
from swagger_client.models.api_list_models_response import ApiListModelsResponse
from swagger_client.models.api_list_notebooks_response import ApiListNotebooksResponse
from swagger_client.models.api_list_pipelines_response import ApiListPipelinesResponse
from swagger_client.models.api_metadata import ApiMetadata
from swagger_client.models.api_model_framework import ApiModelFramework
from swagger_client.models.api_model_framework_runtimes import ApiModelFrameworkRuntimes
from swagger_client.models.api_model_script import ApiModelScript
from swagger_client.models.api_parameter import ApiParameter
from swagger_client.models.api_pipeline import ApiPipeline
from swagger_client.models.api_pipeline_custom import ApiPipelineCustom
from swagger_client.models.api_pipeline_custom_run_payload import (  # noqa: F401
    ApiPipelineCustomRunPayload,
)
from swagger_client.models.api_pipeline_dag import ApiPipelineDAG
from swagger_client.models.api_pipeline_extension import ApiPipelineExtension
from swagger_client.models.api_pipeline_inputs import ApiPipelineInputs
from swagger_client.models.api_pipeline_task import ApiPipelineTask
from swagger_client.models.api_pipeline_task_arguments import ApiPipelineTaskArguments
from swagger_client.models.api_run_code_response import ApiRunCodeResponse
from swagger_client.models.api_settings import ApiSettings
from swagger_client.models.api_settings_section import ApiSettingsSection  # noqa: F401
from swagger_client.models.api_status import ApiStatus
from swagger_client.models.api_url import ApiUrl
from swagger_client.models.dictionary import Dictionary
from swagger_client.models.protobuf_any import ProtobufAny
from swagger_client.models.api_catalog_upload_error import ApiCatalogUploadError
from swagger_client.models.api_catalog_upload_response import ApiCatalogUploadResponse
from swagger_client.models.api_component import ApiComponent
from swagger_client.models.api_dataset import ApiDataset
from swagger_client.models.api_model import ApiModel
from swagger_client.models.api_notebook import ApiNotebook
from swagger_client.models.api_pipeline_extended import ApiPipelineExtended
