from  nyfedapi import ambs
import pandas as pd

def test_ambs_latest():
    assert isinstance(ambs.latest(operation="all", status="results", include="summary"), pd.DataFrame)
    assert isinstance(ambs.latest(operation="all", status="announcements", include="details"), pd.DataFrame)


def test_ambs_results_last_two_weeks():
    assert isinstance(ambs.results_last_two_weeks(operation="all", include="summary"), pd.DataFrame)
    assert isinstance(ambs.results_last_two_weeks(operation="all", include="details"), pd.DataFrame)


def test_ambs_results_last_number():
    assert isinstance(ambs.results_last_number(operation="all", include="summary", number=5), pd.DataFrame)
    assert isinstance(ambs.results_last_number(operation="all", include="details", number=5), pd.DataFrame)


def test_ambs_results_search():
    assert isinstance(ambs.results_search(operation="all", include="summary"), pd.DataFrame)
    assert isinstance(ambs.results_search(operation="all", include="details", startDate="2021-01-01", endDate="2021-01-02"), pd.DataFrame)

