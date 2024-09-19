from nyfedapi import __get_data
import pandas

__all__ = ["latest", "results_last_two_weeks", "results_last_number", "results_search", "reverserepo_propositions_search"]

def latest(operation_type: str, method: str, status: str) -> pandas.DataFrame:
    """
    Returns the latest Repo and/or Reverse Repo operations Announcements or Results for the current day.

    Args:
        operation_type (str): The operation type. Available values : all, repo, reverserepo.
        method (str): The operation method. Available values : all, fixed, single, multiple.
        status (str): The operation status. Available values : announcements, results.

    Returns:
        pandas.DataFrame: Current date operations.
    """
    return __get_data(endpoint=f"/api/rp/{operation_type}/{method}/{status}/latest.csv")
    

def results_last_two_weeks(operation_type: str, method: str) -> pandas.DataFrame:
    """
    Returns the last two weeks Repo and/or Reverse Repo operations Results.

    Args:
        operation_type (str): The operation type. Available values : all, repo, reverserepo.
        method (str): The operation method. Available values : all, fixed, single, multiple.

    Returns:
        pandas.DataFrame: Operations within last two weeks.
    """
    return __get_data(endpoint=f"/api/rp/{operation_type}/{method}/results/lastTwoWeeks.csv")
    

def results_last_number(operation_type: str, method: str, number: int) -> pandas.DataFrame:
    """
    Returns the last N number of Repo and/or Reverse Repo operations Results.

    Args:
        operation_type (str): The operation type. Available values : all, repo, reverserepo.
        method (str): The operation method. Available values : all, fixed, single, multiple.
        number (int): The last N amount of operations to return.

    Returns:
        pandas.DataFrame: Last n number of operations.
    """
    return __get_data(endpoint=f"/api/rp/{operation_type}/{method}/results/last/{number}.csv")
    

def results_search(**kwargs) -> pandas.DataFrame:
    """
    Returns Repo and/or Reverse Repo operation Results.

    Keyword Args:
        startDate (str): The start date (inclusive) from which to search. Format YYYY-MM-DD.
        endDate (str): The end date (inclusive) up until which to search. Format YYYY-MM-DD.
        operationTypes (str): The operation types (comma-delimited) by which to filter. Available values : Repo, Reverse Repo.
        method (str): The operation method by which to filter. Available values : multiple, single, fixed.
        securityType (str): The security type (tranche) by which to filter. For specific types, only operations which include that type will be returned. Available values : mbs, agency, tsy, srf.
        term (str): The term of the operation. Available values : overnight, term.

    Returns:
        pandas.DataFrame: Filter operations.
    """
    return __get_data(endpoint=f"/api/rp/results/search.csv", **kwargs)
    

def reverserepo_propositions_search(**kwargs) -> pandas.DataFrame:
    """
    Returns Propositions for Reverse Repo operations.

    Keyword Args:
        startDate (str): The start date (inclusive) from which to search. Format YYYY-MM-DD.
        endDate (str): The end date (inclusive) up until which to search. Format YYYY-MM-DD.

    Returns:
        pandas.DataFrame: Filter Reverse Repo propositions.
    """
    return __get_data(endpoint=f"/api/rp/reverserepo/propositions/search.csv", **kwargs)
    