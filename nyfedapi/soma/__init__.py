from nyfedapi import __get_data
import pandas

__all__ = ["asofdates_latest", "summary", "asofdates_list", "agency_get_release_log", "agency_get_asof", "agency_get_cusip", "agency_get_holdingtype_asof", "agency_wam_asof", "tsy_get_release_log", "tsy_get_asof", "tsy_get_cusip", "tsy_get_holdingtype_asof", "tsy_wam_holdingtype_asof", "tsy_get_monthly"]

def asofdates_latest() -> pandas.DataFrame:
    """
    Returns the latest SOMA holdings As Of Date.

    Returns:
        pandas.DataFrame: Last As Of Date.
    """
    return __get_data(endpoint=f"/api/soma/asofdates/latest.csv")


def summary() -> pandas.DataFrame:
    """
    Returns Summary Of SOMA holdings for each As of Date and holding type.

    Returns:
        pandas.DataFrame: Total by Security Type.
    """
    return __get_data(endpoint=f"/api/soma/summary.csv")


def asofdates_list() -> pandas.DataFrame:
    """
    Returns all SOMA holdings As of Date.

    Returns:
        pandas.DataFrame: List of As Of Dates.
    """
    return __get_data(endpoint=f"/api/soma/asofdates/list.csv")


def agency_get_release_log() -> pandas.DataFrame:
    """
    Returns the last three months Agency Release and As Of Dates.

    Returns:
        pandas.DataFrame: List of Releases Dates for Agency Securities.
    """
    return __get_data(endpoint=f"/api/soma/agency/get/release_log.csv")


def agency_get_asof(date: str) -> pandas.DataFrame:
    """
    Returns a single date SOMA Agency Holdings.

    Args:
        date (str): The date for which to retrieve the agency release. Format YYYY-MM-DD.

    Returns:
        pandas.DataFrame: Agency Securities by As Of Date.
    """
    return __get_data(endpoint=f"/api/soma/agency/get/asof/{date}.csv")


def agency_get_cusip(cusip: str) -> pandas.DataFrame:
    """
    Returns all SOMA Agency Holdings for a single CUSIP.

    Args:
        cusip (str): The CUSIP for which to retrieve information.

    Returns:
        pandas.DataFrame: Agency Securities by CUSIP.
    """
    return __get_data(endpoint=f"/api/soma/agency/get/cusip/{cusip}.csv")


def agency_get_holdingtype_asof(holding_type: str, date: str) -> pandas.DataFrame:
    """
    Returns a single date SOMA Agency Holdings for a Agency holding type.

    Args:
        holding_type (str): The holding type for which to retrieve. Available values : all, agency debts, mbs, cmbs.
        date (str): The date for which to retrieve the agency release. Format YYYY-MM-DD.

    Returns:
        pandas.DataFrame: Agency Securities by Holding Type and As Of Date.
    """
    return __get_data(endpoint=f"/api/soma/agency/get/{holding_type}/asof/{date}.csv")


def agency_wam_asof(date: str) -> pandas.DataFrame:
    """
    Returns a single date Weighted Average Maturity for Agency Debt.

    Args:
        date (str): The date for which to retrieve the Weighted Average Maturity number. Format YYYY-MM-DD.

    Returns:
        pandas.DataFrame: Agency Debt Weighted Average Maturity by As Of Date.
    """
    return __get_data(endpoint=f"/api/soma/agency/wam/agency%20debts/asof/{date}.csv")


def tsy_get_release_log() -> pandas.DataFrame:
    """
    Returns the last three months Treasury Release and As Of Dates.

    Returns:
        pandas.DataFrame: List of Releases Dates for Treasury Securities.
    """
    return __get_data(endpoint=f"/api/soma/tsy/get/release_log.csv")


def tsy_get_asof(date: str) -> pandas.DataFrame:
    """
    Returns a single date SOMA Treasury Holdings.

    Args:
        date (str): The date for which to retrieve the Treasury release. Format YYYY-MM-DD.

    Returns:
        pandas.DataFrame: Treasury Securities by As Of Date.
    """
    return __get_data(endpoint=f"/api/soma/tsy/get/asof/{date}.csv")


def tsy_get_cusip(cusip: str) -> pandas.DataFrame:
    """
    Returns all SOMA Treasury Holdings for a single CUSIP.

    Args:
        cusip (str): The CUSIP for which to retrieve information.

    Returns:
        pandas.DataFrame: Treasury Securities by CUSIP.
    """
    return __get_data(endpoint=f"/api/soma/tsy/get/cusip/{cusip}.csv")


def tsy_get_holdingtype_asof(holding_type: str, date: str) -> pandas.DataFrame:
    """
    Returns a single date SOMA Agency Holdings for a Treasury holding type.

    Args:
        holding_type (str): The holding type for which to retrieve. Available values : all, bills, notesbonds, frn, tips.
        date (str): The date for which to retrieve the Treasury release. Format YYYY-MM-DD.

    Returns:
        pandas.DataFrame: Treasury Securities by Holding Type and As Of Date.
    """
    return __get_data(endpoint=f"/api/soma/tsy/get/{holding_type}/asof/{date}.csv")


def tsy_wam_holdingtype_asof(holding_type: str, date: str) -> pandas.DataFrame:
    """
    Returns a single date Weighted Average Maturity for a Treasury holding type.

    Args:
        date (str): The date for which to retrieve the Weighted Average Maturity number. Format YYYY-MM-DD.

    Returns:
        pandas.DataFrame: Treasury Debt Weighted Average Maturity by Holding Type As Of Date.
    """
    return __get_data(endpoint=f"/api/soma/tsy/wam/{holding_type}/asof/{date}.csv")


def tsy_get_monthly() -> pandas.DataFrame:
    """
    Returns all SOMA Treasury Holdings at monthly intervals.

    Returns:
        pandas.DataFrame: Monthly summary of Treasury Holdings.
    """
    return __get_data(endpoint=f"/api/soma/tsy/get/monthly.csv")
