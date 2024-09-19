from . import __base_url
import pandas as pd


def qtrly_latest() -> pd.DataFrame:
    """
    Returns the latest quarterly Market Share.

    TODO:
        * Make it work. Currently unusable. Implement logic of qtrly_latest()

    Returns:
        pd.DataFrame: Latest quarterly marketshare data.
    """
    return pd.read_json(f"{__base_url}/api/marketshare/qtrly/latest.json")


def ytd_latest() -> pd.DataFrame:
    """
    Returns the latest year-to-date Market Share.

    TODO:
        * Make it work. Currently unusable. Implement logic of ytd_latest()

    Returns:
        pd.DataFrame: Latest year-to-date marketshare data.
    """
    return pd.read_json(f"{__base_url}/api/marketshare/ytd/latest.json")
