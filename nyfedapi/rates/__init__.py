from nyfedapi import __get_data
import pandas

__all__ = ["all_latest", "all_search", "secured_all_latest", "secured_last_number", "secured_search", "unsecured_all_latest", "unsecured_last_number", "unsecured_search"]

def all_latest() -> pandas.DataFrame:
    """
    Returns the latest secured and unsecured rates.

    Returns:
        pandas.DataFrame: Last As Of Date from current date rates.
    """
    return __get_data(endpoint=f"/api/rates/all/latest.csv")
    

def all_search(**kwargs) -> pandas.DataFrame:
    """
    Returns secured and/or unsecured rates and/or volume.

    Keyword Args:
        startDate (str): The start date (inclusive) from which to search. Defaults to the current date. Format YYYY-MM-DD.
        endDate (str): The end date (inclusive) up until which to search. Format YYYY-MM-DD.
        type (str): The report type to return. Available values : rate, volume.

    Returns:
        pandas.DataFrame: Filter rates.
    """
    return __get_data(endpoint=f"/api/rates/all/search.csv", **kwargs)
    

def secured_all_latest() -> pandas.DataFrame:
    """
    Returns the latest secured rates.

    Returns:
        pandas.DataFrame: Last As Of Date from current date for Secured rates.
    """
    return __get_data(endpoint=f"/api/rates/secured/all/latest.csv")
    

def secured_last_number(ratetype: str, number: int) -> pandas.DataFrame:
    """
    Returns the last N number of secured rates.

    Args:
        ratetype (str): The rate type. Available values : tgcr, bgcr, sofr, sofrai.
        number (int): The last N amount of rates to return.

    Returns:
        pandas.DataFrame: Last n number of Secured rates.
    """
    return __get_data(endpoint=f"/api/rates/secured/{ratetype}/last/{number}.csv")
    

def secured_search(ratetype: str, **kwargs) -> pandas.DataFrame:
    """
    Returns secured rates and/or volume.

    Args:
        ratetype (str): The rate type. Available values : all, tgcr, bgcr, sofr, sofrai.

    Keyword Args:
        startDate (str): The start date (inclusive) from which to search. Defaults to the current date. Format YYYY-MM-DD.
        endDate (str): The end date (inclusive) up until which to search. Format YYYY-MM-DD.
        type (str): The report type to return. Available values : rate, volume

    Returns:
        pandas.DataFrame: Filter Secured rates.
    """
    return __get_data(endpoint=f"/api/rates/secured/{ratetype}/search.csv", **kwargs)
    

def unsecured_all_latest() -> pandas.DataFrame:
    """
    Returns the latest unsecured rates.

    Returns:
        pandas.DataFrame: Last As Of Date from current date for Unsecured rates.
    """
    return __get_data(endpoint=f"/api/rates/unsecured/all/latest.csv")
    

def unsecured_last_number(ratetype: str, number: int) -> pandas.DataFrame:
    """
    Returns the last N number of unsecured rates.

    Args:
        ratetype (str): The rate type. Available values : effr, obfr
        number (int): The last N amount of rates to return.

    Returns:
        pandas.DataFrame: Last n number of Unsecured rates.
    """
    return __get_data(endpoint=f"/api/rates/unsecured/{ratetype}/last/{number}.csv")
    

def unsecured_search(ratetype: str, **kwargs) -> pandas.DataFrame:
    """
    Returns unsecured rates and/or volume.

    Args:
        ratetype (str): The rate type. Available values : all, effr, obfr

    Keyword Args:
        startDate (str): The start date (inclusive) from which to search. Defaults to the current date. Format YYYY-MM-DD.
        endDate (str): The end date (inclusive) up until which to search. Format YYYY-MM-DD.
        type (str): The report type to return. Available values : rate, volume

    Returns:
        pandas.DataFrame: Filter Unsecured rates.
    """
    return __get_data(endpoint=f"/api/rates/unsecured/{ratetype}/search.csv", **kwargs)
