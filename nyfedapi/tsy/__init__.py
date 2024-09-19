from nyfedapi import __get_data
import pandas

__all__ = ["latest", "results_last_two_weeks", "results_last_number", "results_search"]

def latest(operation: str, status: str, include: str) -> pandas.DataFrame:
    """
    Returns the latest Treasury operation Announcements or Results for the current day.

    Args:
        operation (str): The operation type. Available values : all, purchases, sales.
        status (str): The operation status. Available values : announcements, results, operations.
        include (str): The level of details to include. Available values : summary, details.

    Returns:
        pandas.DataFrame: Current date operations.
    """
    return __get_data(endpoint=f"/api/tsy/{operation}/{status}/{include}/latest.csv")
    

def results_last_two_weeks(operation: str, include: str) -> pandas.DataFrame:
    """
    Returns the last two weeks Treasury operations Results.

    Args:
        operation (str): The operation type. Available values : all, purchases, sales.
        include (str): The level of details to include. Available values : summary, details.

    Returns:
        pandas.DataFrame: Operations within last two weeks.
    """
    return __get_data(endpoint=f"/api/tsy/{operation}/results/{include}/lastTwoWeeks.csv")
    

def results_last_number(operation: str, include: str, number: int) -> pandas.DataFrame:
    """
    Returns the last N number of Treasury operations Results.

    Args:
        operation (str): The operation type. Available values : all, purchases, sales.
        include (str): The level of details to include. Available values : summary, details.
        number (int): The last amount of results to return from current date

    Returns:
        pandas.DataFrame: Last n number of operations.
    """
    return __get_data(endpoint=f"/api/tsy/{operation}/results/{include}/last/{number}.csv")


def results_search(operation: str, include: str, **kwargs) -> pandas.DataFrame:
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
        pandas.DataFrame: Filter operations
    """
    return __get_data(endpoint=f"/api/tsy/{operation}/results/{include}/search.csv", **kwargs)
