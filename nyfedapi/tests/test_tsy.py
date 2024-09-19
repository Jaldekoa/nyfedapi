from nyfedapi import tsy
import pandas as pd

def test_tsy_latest():
    assert isinstance(tsy.latest(operation="all", status="results", include="summary"), pd.DataFrame)


def test_tsy_results_last_two_weeks():
    assert isinstance(tsy.results_last_two_weeks(operation="all", include="summary"), pd.DataFrame)


def test_tsy_results_last_number():
    assert isinstance(tsy.results_last_number(operation="all", include="summary", number=5), pd.DataFrame)


def test_tsy_results_search():
    assert isinstance(tsy.results_search(operation="all", include="summary", start_date="2023-01-01"), pd.DataFrame)
