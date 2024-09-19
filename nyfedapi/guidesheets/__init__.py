from . import __base_url
import pandas as pd


def latest(guidesheet_type: str) -> pd.DataFrame:
    """
    Returns the latest Guide Sheet.

    Todo:
        * Make it work. Currently unusable.

    Args:
        guidesheet_type (str): The guide sheet type. Available values : si, wi, fs.

    Returns:
        pd.DataFrame: Current Guide Sheets.
    """
    return None


def previous(guidesheet_type: str) -> pd.DataFrame:
    """
    Returns the previous Guide Sheet.

    Todo:
        * Make it work. Currently unusable.

    Args:
        guidesheet_type (str): The guide sheet type. Available values : si, wi, fs.

    Returns:
        pd.DataFrame: Previously Posted Guide Sheets.
    """
    return None