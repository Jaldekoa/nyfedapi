from nyfedapi import rp
import pandas as pd

def test_rp_latest():
    assert isinstance(rp.latest(operation_type="all", method="all", status="announcements"), pd.DataFrame)
    assert isinstance(rp.latest(operation_type="repo", method="fixed", status="results"), pd.DataFrame)


def test_rp_results_last_two_weeks():
    assert isinstance(rp.results_last_two_weeks(operation_type="all", method="all"), pd.DataFrame)


def test_rp_results_last_number():
    assert isinstance(rp.results_last_number(operation_type="all", method="all", number=5), pd.DataFrame)


def test_rp_results_search():
    assert isinstance(rp.results_search(), pd.DataFrame)


def test_rp_reverserepo_propositions_search():
    assert isinstance(rp.reverserepo_propositions_search(), pd.DataFrame)
