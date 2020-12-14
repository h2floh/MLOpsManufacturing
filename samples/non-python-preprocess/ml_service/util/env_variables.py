"""Env dataclass to load and hold all environment variables
"""
from dataclasses import dataclass
import os
from typing import Optional

from dotenv import load_dotenv


@dataclass(frozen=True)
class Env:
    """Loads all environment variables into a predefined set of properties
    """

    # to load .env file into environment variables for local execution
    load_dotenv()

    # variables from Azure DevOps variable group
    subscription_id: Optional[str] = os.environ.get("SUBSCRIPTION_ID")
    resource_group: Optional[str] = os.environ.get("RESOURCE_GROUP")
    workspace_name: Optional[str] = os.environ.get("WORKSPACE_NAME")

    # variables from variables-template.yml
    sources_directory_train: Optional[str] = os.environ.get("SOURCES_DIR_TRAIN")  # NOQA: E501
    experiment_name: Optional[str] = os.environ.get("EXPERIMENT_NAME")  # NOQA: E501
    dataset_name: Optional[str] = os.environ.get("DATASET_NAME")
    datastore_name: Optional[str] = os.environ.get("DATASTORE_NAME")  # NOQA: E501
    run_evaluation: Optional[str] = os.environ.get("RUN_EVALUATION", "true")  # NOQA: E501
    allow_run_cancel: Optional[str] = os.environ.get("ALLOW_RUN_CANCEL", "true")  # NOQA: E501
    rebuild_env: Optional[bool] = os.environ.get("AML_REBUILD_ENVIRONMENT", "false").lower().strip() == "true"  # NOQA: E501
    vm_size: Optional[str] = os.environ.get("AML_COMPUTE_CLUSTER_CPU_SKU")
    compute_name: Optional[str] = os.environ.get("AML_COMPUTE_CLUSTER_NAME")
    vm_priority: Optional[str] = os.environ.get("AML_CLUSTER_PRIORITY", "lowpriority")  # NOQA: E501
    min_nodes: int = int(os.environ.get("AML_CLUSTER_MIN_NODES", 0))
    max_nodes: int = int(os.environ.get("AML_CLUSTER_MAX_NODES", 4))
    aml_preprocessing_custom_docker_env_name: Optional[str] = os.environ.get("AML_PREPROCESSING_CUSTOM_DOCKER_ENV_NAME")  # NOQA: E501
    preprocessing_os_cmd_pipeline_name: Optional[str] = os.environ.get("PREPROCESSING_OS_CMD_PIPELINE_NAME")  # NOQA: E501

    # derived variables
    processed_dataset_name: Optional[str] = f"{dataset_name}_processed"  # NOQA: E501

    # variables generated by Azure DevOps
    # if running locally, provide these manually
    build_id: Optional[str] = os.environ.get("BUILD_BUILDID")
    build_uri: Optional[str] = os.environ.get("BUILD_URI")
    model_version: Optional[str] = os.environ.get("MODEL_VERSION")