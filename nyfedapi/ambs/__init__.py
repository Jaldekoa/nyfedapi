from nyfedapi import __get_data
import pandas

__all__ = ["latest", "results_last_two_weeks", "results_last_number", "results_search"]

def latest(operation: str, status: str, include: str) -> pandas.DataFrame:
    """
    Returns the latest AMBS operation Announcements or Results for the current day.

    Args:
        operation (str): The operation type. Available values: all, purchases, sales, roll, swap.
        status (str): The operation status. Available values: announcements, results.
        include (str): The level of details to include. Available values: summary, details.

    Returns:
        pandas.DataFrame: Current date operations.
    """
    return __get_data(endpoint=f"/api/ambs/{operation}/{status}/{include}/latest.csv")


def results_last_two_weeks(operation: str, include: str) -> pandas.DataFrame:
    """
    Returns the last two weeks AMBS operations Results.

    Args:
        operation (str): The operation type. Available values: all, purchases, sales, roll, swap.
        include (str): The level of details to include. Available values: summary, details.

    Returns:
        pandas.DataFrame: Operations within last two weeks.
    """
    return __get_data(endpoint=f"/api/ambs/{operation}/results/{include}/lastTwoWeeks.csv")


def results_last_number(operation: str, include: str, number: int) -> pandas.DataFrame:
    """
    Returns the last N number of AMBS operations Results.

    Args:
        operation (str): The operation type. Available values: all, purchases, sales, roll, swap.
        include (str): The level of details to include. Available values: summary, details.
        number (int): The last N amount of operations to return.

    Returns:
        pandas.DataFrame: Last n number of operations.
    """
    return __get_data(endpoint=f"/api/ambs/{operation}/results/{include}/last/{number}.csv")


def results_search(operation: str, include: str, **kwargs) -> pandas.DataFrame:
    """
    Returns AMBS operations Results.

    Args:
        operation (str): The operation type. Available values : all, purchases, sales, roll, swap.
        include (str): The level of details to include. Available values : summary, details.

    Keyword Args:
        startDate (str): The start date (inclusive) from which to search. Format YYYY-MM-DD.
        endDate (str): The end date (inclusive) up until which to search. Format YYYY-MM-DD.
        securities (str): Filter by securities (Operation Method). Available values: Basket, Coupon Swap, Dollar Roll, Specified Pool, TBA
        cusip (str): Only return operations which include the given CUSIP. Partial identifiers are accepted.
        desc (str): Only return operations which include the given Security Description. Partial identifiers are accepted.

    Returns:
        pandas.DataFrame: Filter operations.
    """
    return __get_data(endpoint=f"/api/ambs/{operation}/results/{include}/search.csv", **kwargs)
