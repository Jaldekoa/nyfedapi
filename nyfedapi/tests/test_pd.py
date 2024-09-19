import pandas as pd
import nyfedapi


def test_pd_latest():
    assert isinstance(nyfedapi.pd.latest(seriesbreak="SBN2022"), pd.DataFrame)


def test_pd_get_all_timeseries():
    assert isinstance(nyfedapi.pd.get_all_timeseries(), pd.DataFrame)


def test_pd_list_timeseries():
    assert isinstance(nyfedapi.pd.list_timeseries(), pd.DataFrame)


def test_pd_list_asof():
    assert isinstance(nyfedapi.pd.list_asof(), pd.DataFrame)


def test_pd_list_seriesbreaks():
    assert isinstance(nyfedapi.pd.list_seriesbreaks(), pd.DataFrame)


def test_pd_get_asof():
    assert isinstance(nyfedapi.pd.get_asof(date="2023-01-01"), pd.DataFrame)


def test_pd_get_timeseries():
    assert isinstance(nyfedapi.pd.get_timeseries(timeseries="PDPOSGS-B_PDPOSGSC-L2"), pd.DataFrame)


def test_pd_get_seriesbreaks_timeseries():
    assert isinstance(nyfedapi.pd.get_seriesbreaks_timeseries(seriesbreak="SBN2022", timeseries="PDPOSGSC-G11L21_PDPOSGSC-G2"), pd.DataFrame)
