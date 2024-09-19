from nyfedapi import soma
import pandas as pd

def test_soma_asofdates_latest():
    assert isinstance(soma.asofdates_latest(), pd.DataFrame)


def test_soma_summary():
    assert isinstance(soma.summary(), pd.DataFrame)


def test_soma_asofdates_list():
    assert isinstance(soma.asofdates_list(), pd.DataFrame)


def test_soma_agency_get_release_log():
    assert isinstance(soma.agency_get_release_log(), pd.DataFrame)


def test_soma_agency_get_asof():
    assert isinstance(soma.agency_get_asof(date="2023-01-01"), pd.DataFrame)


def test_soma_agency_get_cusip():
    assert isinstance(soma.agency_get_cusip(cusip="3134A4KX1"), pd.DataFrame)


def test_soma_agency_get_holdingtype_asof():
    assert isinstance(soma.agency_get_holdingtype_asof(holding_type="all", date="2023-01-01"), pd.DataFrame)


def test_soma_agency_wam_asof():
    assert isinstance(soma.agency_wam_asof(date="2023-01-01"), pd.DataFrame)


def test_soma_tsy_get_release_log():
    assert isinstance(soma.tsy_get_release_log(), pd.DataFrame)


def test_soma_tsy_get_asof():
    assert isinstance(soma.tsy_get_asof(date="2023-01-01"), pd.DataFrame)


def test_soma_tsy_get_cusip():
    assert isinstance(soma.tsy_get_cusip(cusip="9127963K3"), pd.DataFrame)


def test_soma_tsy_get_holdingtype_asof():
    assert isinstance(soma.tsy_get_holdingtype_asof(holding_type="all", date="2023-01-01"), pd.DataFrame)


def test_soma_tsy_wam_holdingtype_asof():
    assert isinstance(soma.tsy_wam_holdingtype_asof(holding_type="all", date="2023-01-01"), pd.DataFrame)


def test_soma_tsy_get_monthly():
    assert isinstance(soma.tsy_get_monthly(), pd.DataFrame)
