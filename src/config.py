import os
import pathlib
from enum import Enum

from dotenv import load_dotenv
from loguru import logger

from .utils import check_env_variable, ensure_file, ensure_path


class DirectoryPaths(Enum):
    PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
    ENV_FILE = ensure_file(PROJECT_ROOT / ".env")
    DATA = ensure_path(PROJECT_ROOT / "data")
    EXTERNAL_DATA = ensure_path(DATA / "external")


class Environment(Enum):
    """Settings class to hold environment variables."""

    # Example:
    # DATABASE_URL = os.getenv("DATABASE_URL")


_PROJECT_ROOT = DirectoryPaths.PROJECT_ROOT.value
_DATA_DIR = DirectoryPaths.DATA.value
_ENV_FILE = DirectoryPaths.ENV_FILE.value

if _ENV_FILE.exists():
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


# Log key paths
logger.info(f"PROJECT_ROOT: {_PROJECT_ROOT}")
logger.info(f"DATA_DIR: {_DATA_DIR}")
