from nyfedapi import seclending
import pandas as pd

def test_seclending_results_latest():
    assert isinstance(seclending.results_latest(operation="all", include="summary"), pd.DataFrame)
    assert isinstance(seclending.results_latest(operation="all", include="details"), pd.DataFrame)


def test_seclending_results_last_two_weeks():
    assert isinstance(seclending.results_last_two_weeks(operation="all", include="summary"), pd.DataFrame)
    assert isinstance(seclending.results_last_two_weeks(operation="all", include="details"), pd.DataFrame)


def test_seclending_results_last_number():
    assert isinstance(seclending.results_last_number(operation="all", include="summary", number=5), pd.DataFrame)
    assert isinstance(seclending.results_last_number(operation="all", include="details", number=5), pd.DataFrame)


def test_seclending_results_search():
    assert isinstance(seclending.results_search(operation="all", include="summary"), pd.DataFrame)
    assert isinstance(seclending.results_search(operation="all", include="details"), pd.DataFrame)
