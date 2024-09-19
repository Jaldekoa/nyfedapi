from nyfedapi import rates
import pandas as pd

def test_rates_all_latest():
    assert isinstance(rates.all_latest(), pd.DataFrame)


def test_rates_all_search():
    assert isinstance(rates.all_search(), pd.DataFrame)


def test_rates_secured_all_latest():
    assert isinstance(rates.secured_all_latest(), pd.DataFrame)


def test_rates_secured_last_number():
    assert isinstance(rates.secured_last_number(ratetype="tgcr", number=5), pd.DataFrame)
    assert isinstance(rates.secured_last_number(ratetype="bgcr", number=5), pd.DataFrame)
    assert isinstance(rates.secured_last_number(ratetype="sofr", number=5), pd.DataFrame)
    assert isinstance(rates.secured_last_number(ratetype="sofrai", number=5), pd.DataFrame)


def test_rates_secured_search():
    assert isinstance(rates.secured_search(ratetype="bgcr"), pd.DataFrame)


def test_rates_unsecured_all_latest():
    assert isinstance(rates.unsecured_all_latest(), pd.DataFrame)


def test_rates_unsecured_last_number():
    assert isinstance(rates.unsecured_last_number(ratetype="effr", number=5), pd.DataFrame)
    assert isinstance(rates.unsecured_last_number(ratetype="obfr", number=5), pd.DataFrame)


def test_rates_unsecured_search():
    assert isinstance(rates.unsecured_search(ratetype="effr"), pd.DataFrame)
