import os
import pathlib

from dotenv import load_dotenv
from loguru import logger

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()
DATA_DIR = PROJECT_ROOT / "data"

if not (PROJECT_ROOT / ".env").exists():
    raise FileNotFoundError(
        f"Please create a .env file in the root directory ({PROJECT_ROOT})"
    )
else:
    load_dotenv(PROJECT_ROOT / ".env")

    # # Load environment variables
    # DATABASE_URL1 = os.getenv("DATABASE_URL1")
    # DATABASE_URL2 = os.getenv("DATABASE_URL2")

    def check_env_variable(var_name):
        """Check if an environment variable is set."""
        if var_name is None:
            raise EnvironmentError(f"Environment variable {var_name} is not set.")

    ## Check if the environment variables are set
    # check_env_variable(DATABASE_URL1)
    # check_env_variable(DATABASE_URL2)


logger.info(f"PROJECT_ROOT: {PROJECT_ROOT}")
logger.info(f"DATA_DIR: {DATA_DIR}")
