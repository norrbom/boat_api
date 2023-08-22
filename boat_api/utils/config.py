from pathlib import Path
from dotenv import dotenv_values, load_dotenv


def load_config(dotenv_path: str = ".env") -> dict:
    """
    Loads env variables from a .env file
    Returns:
        returns a dict of env variables in dot file
    """
    path = Path(__file__).parent.parent.parent.joinpath(dotenv_path)
    load_dotenv(dotenv_path=path)
    return dotenv_values(dotenv_path=path)
