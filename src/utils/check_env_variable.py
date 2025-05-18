from loguru import logger
import sys


def check_env_variable(var, var_name: str, important: bool = False):
    """Check if an environment variable is set."""
    if var is None:
        if important:
            logger.error(EnvironmentError(f"Environment variable '{var_name}' is not set."))
            sys.exit(1)
        else:
            logger.warning(f"Environment variable {var_name} is not set.")
