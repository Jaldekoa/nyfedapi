from nyfedapi import __get_data
import pandas as pd

__all__ = ["latest", "get_all_timeseries", "list_timeseries", "list_asof", "list_seriesbreaks", "get_asof", "get_timeseries", "get_seriesbreaks_timeseries"]

def latest(seriesbreak: str) -> pd.DataFrame:
    """
    Returns the latest Survey results for each timeseries.

    Args:
        seriesbreak (str): A valid series break value. Available values: SBN2022, SBN2015, SBN2013, SBP2013, SBP2001.

    Returns:
        pd.DataFrame: Last survey by Series Break.
    """
    return __get_data(endpoint=f"/api/pd/latest/{seriesbreak}.csv")


def get_all_timeseries() -> pd.DataFrame:
    """
    Returns all Survey results in csv format.

    Returns:
        pd.DataFrame: All surveys.
    """
    return __get_data(endpoint=f"/api/pd/get/all/timeseries.csv")


def list_timeseries() -> pd.DataFrame:
    """
    Returns Description of timeseries/keyids.

    Returns:
        pd.DataFrame: Definition of Time Series/Key Id
    """
    return __get_data(endpoint=f"/api/pd/list/timeseries.csv")


def list_asof() -> pd.DataFrame:
    """
    Returns all As Of Dates with respective Series Break.

    Returns:
        pd.DataFrame: List of As Of Dates.
    """
    return __get_data(endpoint=f"/api/pd/list/asof.csv")
    

def list_seriesbreaks() -> pd.DataFrame:
    """
    Returns Series Breaks including Label, Start and End Date.

    Returns:
        pd.DataFrame: List of Series Breaks.
    """
    return __get_data(endpoint=f"/api/pd/list/seriesbreaks.csv")


def get_asof(date: str) -> pd.DataFrame:
    """
    Returns single date Survey results.

    Args:
        date (str): The time series as of date. Format YYYY-MM-DD.

    Returns:
        pd.DataFrame: Survey by As Of Date.
    """
    return __get_data(endpoint=f"/api/pd/get/asof/{date}.csv")


def get_timeseries(timeseries: str) -> pd.DataFrame:
    """

    Args:
        timeseries (str): A list of time series ids separated by underscores.

    Returns:
        pd.DataFrame: Survey by Times Series
    """
    return __get_data(endpoint=f"/api/pd/get/{timeseries}.csv")


def get_seriesbreaks_timeseries(seriesbreak: str, timeseries: str):
    """
    Return Survey results for given seriesbreak and timeseries. To query multiple timeseries, separate each with underscore(_).

    Args:
        seriesbreak (str): A valid series break value. Available values: SBN2022, SBN2015, SBN2013, SBP2013, SBP2001.
        timeseries (str): A list of valid time series separated with underscores.

    Returns:
        pd.DataFrame: Survey by Series Break and Times Series.
    """
    return __get_data(endpoint=f"/api/pd/get/{seriesbreak}/timeseries/{timeseries}.csv")
