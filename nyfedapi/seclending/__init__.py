from nyfedapi import __get_data
import pandas

__all__ = ["results_latest", "results_last_two_weeks", "results_last_number", "results_search"]

def results_latest(operation: str, include: str) -> pandas.DataFrame:
    """
    Returns the latest Securities Lending operation Results for the current day.

    Args:
        operation (str): The operation type. Available values : all, seclending, extensions.
        include (str): The level of details to include. Available values : summary, details.

    Returns:
        pandas.DataFrame: Current date operations.
    """
    return __get_data(endpoint=f"/api/seclending/{operation}/results/{include}/latest.csv")
   

def results_last_two_weeks(operation: str, include: str) -> pandas.DataFrame:
    """
    Returns the last two weeks Securities Lending operation Results and/or Extensions.

    Args:
        operation (str): The operation type. Available values : all, seclending, extensions.
        include (str): The level of details to include. Available values : summary, details.

    Returns:
        pandas.DataFrame: Operations within last two weeks.
    """
    return __get_data(endpoint=f"/api/seclending/{operation}/results/{include}/lastTwoWeeks.csv")
   

def results_last_number(operation: str, include: str, number: int) -> pandas.DataFrame:
    """
    Returns the last N number of Securities Lending operation Results and/or Extensions.

    Args:
        operation (str): The operation type. Available values : all, seclending, extensions.
        include (str): The level of details to include. Available values : summary, details.
        number (int): The last N amount of operations to return.

    Returns:
        pandas.DataFrame: Last n number of operations.
    """
    return __get_data(endpoint=f"/api/seclending/{operation}/results/{include}/last/{number}.csv")


def results_search(operation: str, include: str, **kwargs) -> pandas.DataFrame:
    """
    Returns Securities Lending operation Results and/or Extensions.

    Args:
        operation (str): The operation type. Available values : all, seclending, extensions.
        include (str): The level of details to include. Available values : summary, details.

    Keyword Args:
        startDate (str): The start date (inclusive) from which to search. Format YYYY-MM-DD.
        endDate (str): The end date (inclusive) up until which to search. Format YYYY-MM-DD.
        cusips (str): Comma separated list of cusips. Only return operations where CUSIP contains the parameter value(s) provided. Partial identifiers are accepted.
        descriptions (str): Comma separated list of security descriptions. Only return operations where Security Description contains the parameter value(s) provided. Partial identifiers are accepted.

    Returns:
        pandas.DataFrame: Filter operations.
    """
    return __get_data(endpoint=f"/api/seclending/{operation}/results/{include}/search.csv", **kwargs)
