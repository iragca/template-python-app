import os
import pathlib
from enum import Enum

from dotenv import load_dotenv
from loguru import logger

from src.utils import check_env_variable, ensure_path


class DirectoryPaths(Enum):
    PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
    ENV_FILE = ensure_path(PROJECT_ROOT / ".env")
    DATA_DIR = ensure_path(PROJECT_ROOT / "data")


_PROJECT_ROOT = DirectoryPaths.PROJECT_ROOT.value
_DATA_DIR = DirectoryPaths.DATA_DIR.value
_ENV_FILE = DirectoryPaths.ENV_FILE.value

if not _ENV_FILE.exists():
    logger.warning(
        f".env file not found at {_ENV_FILE}. Please create one with the required environment variables."
    )
else:
    load_dotenv(dotenv_path=_ENV_FILE)
    logger.info(f"Loaded environment variables from {_ENV_FILE}")

required_env_vars = []
non_essential_env_vars = []

for var in required_env_vars:
    value = os.getenv(var)
    check_env_variable(value, var, important=True)

for var in non_essential_env_vars:
    value = os.getenv(var)
    check_env_variable(value, var)


class Environment(Enum):
    """Settings class to hold environment variables."""

    # Example:
    # DB_URL = os.getenv("DB_URL")


# Log key paths
logger.info(f"PROJECT_ROOT: {_PROJECT_ROOT}")
logger.info(f"DATA_DIR: {_DATA_DIR}")
