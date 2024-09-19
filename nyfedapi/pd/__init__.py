from nyfedapi import __get_data
import pandas

__all__ = ["latest", "get_all_timeseries", "list_timeseries", "list_asof", "list_seriesbreaks", "get_asof", "get_timeseries", "get_seriesbreaks_timeseries"]

def latest(seriesbreak: str) -> pandas.DataFrame:
    """
    Returns the latest Survey results for each timeseries.

    Args:
        seriesbreak (str): A valid series break value. Available values: SBN2022, SBN2015, SBN2013, SBP2013, SBP2001.

    Returns:
        pandas.DataFrame: Last survey by Series Break.
    """
    return __get_data(endpoint=f"/api/pd/latest/{seriesbreak}.csv")


def get_all_timeseries() -> pandas.DataFrame:
    """
    Returns all Survey results in csv format.

    Returns:
        pandas.DataFrame: All surveys.
    """
    return __get_data(endpoint=f"/api/pd/get/all/timeseries.csv")


def list_timeseries() -> pandas.DataFrame:
    """
    Returns Description of timeseries/keyids.

    Returns:
        pandas.DataFrame: Definition of Time Series/Key Id
    """
    return __get_data(endpoint=f"/api/pd/list/timeseries.csv")


def list_asof() -> pandas.DataFrame:
    """
    Returns all As Of Dates with respective Series Break.

    Returns:
        pandas.DataFrame: List of As Of Dates.
    """
    return __get_data(endpoint=f"/api/pd/list/asof.csv")
    

def list_seriesbreaks() -> pandas.DataFrame:
    """
    Returns Series Breaks including Label, Start and End Date.

    Returns:
        pandas.DataFrame: List of Series Breaks.
    """
    return __get_data(endpoint=f"/api/pd/list/seriesbreaks.csv")


def get_asof(date: str) -> pandas.DataFrame:
    """
    Returns single date Survey results.

    Args:
        date (str): The time series as of date. Format YYYY-MM-DD.

    Returns:
        pandas.DataFrame: Survey by As Of Date.
    """
    return __get_data(endpoint=f"/api/pd/get/asof/{date}.csv")


def get_timeseries(timeseries: str) -> pandas.DataFrame:
    """

    Args:
        timeseries (str): A list of time series ids separated by underscores.

    Returns:
        pandas.DataFrame: Survey by Times Series
    """
    return __get_data(endpoint=f"/api/pd/get/{timeseries}.csv")


def get_seriesbreaks_timeseries(seriesbreak: str, timeseries: str):
    """
    Return Survey results for given seriesbreak and timeseries. To query multiple timeseries, separate each with underscore(_).

    Args:
        seriesbreak (str): A valid series break value. Available values: SBN2022, SBN2015, SBN2013, SBP2013, SBP2001.
        timeseries (str): A list of valid time series separated with underscores.

    Returns:
        pandas.DataFrame: Survey by Series Break and Times Series.
    """
    return __get_data(endpoint=f"/api/pd/get/{seriesbreak}/timeseries/{timeseries}.csv")
