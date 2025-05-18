import os
import pathlib

from dotenv import load_dotenv
from loguru import logger
from src.utils import check_env_variable


PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"
DATA_DIR = PROJECT_ROOT / "data"

if not ENV_FILE.exists():
    logger.warning(
        f".env file not found at {ENV_FILE}. Please create one with the required environment variables."
    )
else:
    load_dotenv(dotenv_path=ENV_FILE)
    logger.info(f"Loaded environment variables from {ENV_FILE}")

required_env_vars = ["test"]
non_essential_env_vars = []

for var in required_env_vars:
    value = os.getenv(var)
    check_env_variable(value, var, important=True)

for var in non_essential_env_vars:
    value = os.getenv(var)
    check_env_variable(value, var)


class Settings:
    """Settings class to hold environment variables."""

    def __init__(self):
        self.test = os.getenv("test")
        # Add more environment variables as needed
        # self.another_var = os.getenv("another_var")


# Log key paths
logger.info(f"PROJECT_ROOT: {PROJECT_ROOT}")
logger.info(f"DATA_DIR: {DATA_DIR}")
