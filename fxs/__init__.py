from nyfedapi import __get_data
import pandas as pd

__all__ = ["latest", "last_number", "search", "list_counterparties"]

def latest(operation_type: str) -> pd.DataFrame:
    """
    Returns the latest Liquidity Swaps operation Results posted on current day.

    Args:
        operation_type (str): The operation type to search for. Available values : all, usdollar, nonusdollar.

    Returns:
        pd.DataFrame: Current date posted operations.
    """
    return __get_data(endpoint=f"/api/fxs/{operation_type}/latest.csv")


def last_number(operation_type: str, number: int) -> pd.DataFrame:
    """
    Returns the last N number of Liquidity Swaps operations Results.

    Args:
        operation_type (str): The operation type to search for. Available values : all, usdollar, nonusdollar.
        number (int): The last N amount of trades to return.

    Returns:
        pd.DataFrame: Last n number of operations.
    """
    return __get_data(endpoint=f"/api/fxs/{operation_type}/last/{number}.csv")


def search(operation_type: str, **kwargs) -> pd.DataFrame:
    """

    Args:
        operation_type (str): The operation type to search for. Available values : all, usdollar, nonusdollar.

    Keyword Args:
        startDate (str): The start date (inclusive) from which to search, depending on date type. Defaults to current date. Format YYYY-MM-DD.
        endDate (str): The end date (inclusive) up until which to search, depending on date type.  Format YYYY-MM-DD.
        dateType (str): The date type to search for within the start and end. Defaults to trade date. Available values : trade, maturity.
        counterparties (str): A comma-separated list of counterparty names to search for. Partial names are accepted.

    Returns:
        pd.DataFrame: Filter operations.
    """
    return __get_data(endpoint=f"/api/fxs/{operation_type}/search.csv", **kwargs)


def list_counterparties() -> pd.DataFrame:
    """
    Returns Counterparties of Liquidity Swaps operations.

    Returns:
        pd.DataFrame: List of Counterparties.
    """
    return __get_data(endpoint=f"/api/fxs/list/counterparties.csv")
