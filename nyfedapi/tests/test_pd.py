from nyfedapi.pd import latest, get_all_timeseries, list_timeseries, list_asof, list_seriesbreaks, get_asof, get_timeseries, get_seriesbreaks_timeseries
import pandas


def test_pd_latest():
    assert isinstance(latest(seriesbreak="SBN2022"), pandas.DataFrame)


def test_pd_get_all_timeseries():
    assert isinstance(get_all_timeseries(), pandas.DataFrame)


def test_pd_list_timeseries():
    assert isinstance(list_timeseries(), pandas.DataFrame)


def test_pd_list_asof():
    assert isinstance(list_asof(), pandas.DataFrame)


def test_pd_list_seriesbreaks():
    assert isinstance(list_seriesbreaks(), pandas.DataFrame)


def test_pd_get_asof():
    assert isinstance(get_asof(date="2023-01-01"), pandas.DataFrame)


def test_pd_get_timeseries():
    assert isinstance(get_timeseries(timeseries="PDPOSGS-B_PDPOSGSC-L2"), pandas.DataFrame)


def test_pd_get_seriesbreaks_timeseries():
    assert isinstance(get_seriesbreaks_timeseries(seriesbreak="SBN2022", timeseries="PDPOSGSC-G11L21_PDPOSGSC-G2"), pandas.DataFrame)
