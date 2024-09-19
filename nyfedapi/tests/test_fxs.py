from nyfedapi import fxs
import pandas as pd

def test_fxs_latest():
    assert isinstance(fxs.latest(operation_type="all"), pd.DataFrame)


def test_fxs_last_number():
    assert isinstance(fxs.last_number(operation_type="usdollar", number=5), pd.DataFrame)
    assert isinstance(fxs.last_number(operation_type="nonusdollar", number=5), pd.DataFrame)


def test_fxs_search():
    assert isinstance(fxs.search(operation_type="all"), pd.DataFrame)
    assert isinstance(fxs.search(operation_type="all", start_date="2023-01-01", end_date="2023-12-31", date_type="maturity"), pd.DataFrame)


def test_fxs_list_counterparties():
    assert isinstance(fxs.list_counterparties(), pd.DataFrame)
