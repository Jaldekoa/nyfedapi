from urllib.parse import urlencode
from . import __base_url
import pandas as pd


def latest(operation: str, status: str, include: str) -> pd.DataFrame:
    """
    Returns the latest Treasury operation Announcements or Results for the current day.

    Args:
        operation (str): The operation type. Available values : all, purchases, sales.
        status (str): The operation status. Available values : announcements, results, operations.
        include (str): The level of details to include. Available values : summary, details.

    Returns:
        pd.DataFrame: Current date operations.
    """
    return pd.read_csv(f"{__base_url}/api/tsy/{operation}/{status}/{include}/latest.csv")


def results_last_two_weeks(operation: str, include: str) -> pd.DataFrame:
    """
    Returns the last two weeks Treasury operations Results.

    Args:
        operation (str): The operation type. Available values : all, purchases, sales.
        include (str): The level of details to include. Available values : summary, details.

    Returns:
        pd.DataFrame: Operations within last two weeks.
    """
    return pd.read_csv(f"{__base_url}/api/tsy/{operation}/results/{include}/lastTwoWeeks.csv")


def results_last_number(operation: str, include: str, number: int) -> pd.DataFrame:
    """
    Returns the last N number of Treasury operations Results.

    Args:
        operation (str): The operation type. Available values : all, purchases, sales.
        include (str): The level of details to include. Available values : summary, details.
        number (int): The last amount of results to return from current date

    Returns:
        pd.DataFrame: Last n number of operations.
    """
    return pd.read_csv(f"{__base_url}/api/tsy/{operation}/results/{include}/last/{number}.csv")


def results_search(operation: str, include: str, **kwargs) -> pd.DataFrame:
    """
    Returns Treasury operation Results.

    Args:
        operation (str): The operation type. Available values : all, purchases, sales.
        include (str): The level of details to include. Available values : summary, details.

    Keyword Args:
        startDate (str): The start date (inclusive) from which to search. Format YYYY-MM-DD.
        endDate (str): The end date (inclusive) up until which to search. Format YYYY-MM-DD.
        securityType (str): Filter by security type. "agency" include Agency Debt. "treasury" includes Bill, Coupon, FRN, TIPS, and Other. Available values : agency, treasury.
        cusip (str): Only return operations which include the given CUSIP. Partial identifiers are accepted.
        desc (str): Only return operations which include the given Security Description. Partial identifiers are accepted.

    Returns:
        pd.DataFrame: Filter operations
    """
    return pd.read_csv(f"{__base_url}/api/tsy/{operation}/results/{include}/search.csv?{urlencode(kwargs)}")
