from nyfedapi import ambs, fxs, guidesheets, marketshare, pd, rates, rp, seclending, soma, tsy
import pandas
import pytest


# Agency Mortgage-Backed Securities Operations
def test_ambs_latest():
    assert isinstance(ambs.latest(operation="all", status="results", include="summary"), pandas.DataFrame)
    assert isinstance(ambs.latest(operation="all", status="announcements", include="details"), pandas.DataFrame)


def test_ambs_results_last_two_weeks():
    assert isinstance(ambs.results_last_two_weeks(operation="all", include="summary"), pandas.DataFrame)
    assert isinstance(ambs.results_last_two_weeks(operation="all", include="details"), pandas.DataFrame)


def test_ambs_results_last_number():
    assert isinstance(ambs.results_last_number(operation="all", include="summary", number=5), pandas.DataFrame)
    assert isinstance(ambs.results_last_number(operation="all", include="details", number=5), pandas.DataFrame)


def test_ambs_results_search():
    assert isinstance(ambs.results_search(operation="all", include="summary"), pandas.DataFrame)
    assert isinstance(ambs.results_search(operation="all", include="details", startDate="2021-01-01", endDate="2021-01-02"), pandas.DataFrame)


# Central Bank Liquidity Swaps Operations
def test_fxs_latest():
    assert isinstance(fxs.latest(operation_type="all"), pandas.DataFrame)


def test_fxs_last_number():
    assert isinstance(fxs.last_number(operation_type="usdollar", number=5), pandas.DataFrame)
    assert isinstance(fxs.last_number(operation_type="nonusdollar", number=5), pandas.DataFrame)


def test_fxs_search():
    assert isinstance(fxs.search(operation_type="all"), pandas.DataFrame)
    assert isinstance(fxs.search(operation_type="all", start_date="2023-01-01", end_date="2023-12-31", date_type="maturity"), pandas.DataFrame)


def test_fxs_list_counterparties():
    assert isinstance(fxs.list_counterparties(), pandas.DataFrame)


# Guide Sheets
def test_guidesheets_latest():
    assert isinstance(guidesheets.latest(guidesheet_type="si"), pandas.DataFrame)
    assert isinstance(guidesheets.latest(guidesheet_type="wi"), pandas.DataFrame)
    assert isinstance(guidesheets.latest(guidesheet_type="fs"), pandas.DataFrame)


def test_guidesheets_previous():
    assert isinstance(guidesheets.previous(guidesheet_type="si"), pandas.DataFrame)
    assert isinstance(guidesheets.previous(guidesheet_type="wi"), pandas.DataFrame)
    assert isinstance(guidesheets.previous(guidesheet_type="fs"), pandas.DataFrame)


@pytest.mark.skip
# Primary Dealer Statistics Market Share
def test_marketshare_qtrly_latest():
    assert isinstance(marketshare.qtrly_latest(), pandas.DataFrame)


@pytest.mark.skip
def test_marketshare_ytd_latest():
    assert isinstance(marketshare.ytd_latest(), pandas.DataFrame)


# Primary Dealer Statistics
def test_pd_latest():
    assert isinstance(pd.latest(seriesbreak="SBN2022"), pandas.DataFrame)


def test_pd_get_all_timeseries():
    assert isinstance(pd.get_all_timeseries(), pandas.DataFrame)


def test_pd_list_timeseries():
    assert isinstance(pd.list_timeseries(), pandas.DataFrame)


def test_pd_list_asof():
    assert isinstance(pd.list_asof(), pandas.DataFrame)


def test_pd_list_seriesbreaks():
    assert isinstance(pd.list_seriesbreaks(), pandas.DataFrame)


def test_pd_get_asof():
    assert isinstance(pd.get_asof(date="2023-01-01"), pandas.DataFrame)


def test_pd_get_timeseries():
    assert isinstance(pd.get_timeseries(timeseries="PDPOSGS-B_PDPOSGSC-L2"), pandas.DataFrame)


def test_pd_get_seriesbreaks_timeseries():
    assert isinstance(pd.get_seriesbreaks_timeseries(seriesbreak="SBN2022", timeseries="PDPOSGSC-G11L21_PDPOSGSC-G2"), pandas.DataFrame)


# Reference Rates
def test_rates_all_latest():
    assert isinstance(rates.all_latest(), pandas.DataFrame)


def test_rates_all_search():
    assert isinstance(rates.all_search(), pandas.DataFrame)


def test_rates_secured_all_latest():
    assert isinstance(rates.secured_all_latest(), pandas.DataFrame)


def test_rates_secured_last_number():
    assert isinstance(rates.secured_last_number(ratetype="tgcr", number=5), pandas.DataFrame)
    assert isinstance(rates.secured_last_number(ratetype="bgcr", number=5), pandas.DataFrame)
    assert isinstance(rates.secured_last_number(ratetype="sofr", number=5), pandas.DataFrame)
    assert isinstance(rates.secured_last_number(ratetype="sofrai", number=5), pandas.DataFrame)


def test_rates_secured_search():
    assert isinstance(rates.secured_search(ratetype="bgcr"), pandas.DataFrame)


def test_rates_unsecured_all_latest():
    assert isinstance(rates.unsecured_all_latest(), pandas.DataFrame)


def test_rates_unsecured_last_number():
    assert isinstance(rates.unsecured_last_number(ratetype="effr", number=5), pandas.DataFrame)
    assert isinstance(rates.unsecured_last_number(ratetype="obfr", number=5), pandas.DataFrame)


def test_rates_unsecured_search():
    assert isinstance(rates.unsecured_search(ratetype="effr"), pandas.DataFrame)


# Repo and Reverse Repo Operations
def test_rp_latest():
    assert isinstance(rp.latest(operation_type="all", method="all", status="announcements"), pandas.DataFrame)
    assert isinstance(rp.latest(operation_type="repo", method="fixed", status="results"), pandas.DataFrame)


def test_rp_results_last_two_weeks():
    assert isinstance(rp.results_last_two_weeks(operation_type="all", method="all"), pandas.DataFrame)


def test_rp_results_last_number():
    assert isinstance(rp.results_last_number(operation_type="all", method="all", number=5), pandas.DataFrame)


def test_rp_results_search():
    assert isinstance(rp.results_search(), pandas.DataFrame)


def test_rp_reverserepo_propositions_search():
    assert isinstance(rp.reverserepo_propositions_search(), pandas.DataFrame)


# Securities Lending Operations
def test_seclending_results_latest():
    assert isinstance(seclending.results_latest(operation="all", include="summary"), pandas.DataFrame)
    assert isinstance(seclending.results_latest(operation="all", include="details"), pandas.DataFrame)


def test_seclending_results_last_two_weeks():
    assert isinstance(seclending.results_last_two_weeks(operation="all", include="summary"), pandas.DataFrame)
    assert isinstance(seclending.results_last_two_weeks(operation="all", include="details"), pandas.DataFrame)


def test_seclending_results_last_number():
    assert isinstance(seclending.results_last_number(operation="all", include="summary", number=5), pandas.DataFrame)
    assert isinstance(seclending.results_last_number(operation="all", include="details", number=5), pandas.DataFrame)


@pytest.mark.skip
def test_seclending_results_search():
    assert isinstance(seclending.results_search(operation="all", include="summary"), pandas.DataFrame)
    assert isinstance(seclending.results_search(operation="all", include="details"), pandas.DataFrame)


# System Open Market Account Holdings
def test_soma_asofdates_latest():
    assert isinstance(soma.asofdates_latest(), pandas.DataFrame)


def test_soma_summary():
    assert isinstance(soma.summary(), pandas.DataFrame)


def test_soma_asofdates_list():
    assert isinstance(soma.asofdates_list(), pandas.DataFrame)


def test_soma_agency_get_release_log():
    assert isinstance(soma.agency_get_release_log(), pandas.DataFrame)


def test_soma_agency_get_asof():
    assert isinstance(soma.agency_get_asof(date="2023-01-01"), pandas.DataFrame)


def test_soma_agency_get_cusip():
    assert isinstance(soma.agency_get_cusip(cusip="3134A4KX1"), pandas.DataFrame)


def test_soma_agency_get_holdingtype_asof():
    assert isinstance(soma.agency_get_holdingtype_asof(holding_type="all", date="2023-01-01"), pandas.DataFrame)


def test_soma_agency_wam_asof():
    assert isinstance(soma.agency_wam_asof(date="2023-01-01"), pandas.DataFrame)


def test_soma_tsy_get_release_log():
    assert isinstance(soma.tsy_get_release_log(), pandas.DataFrame)


def test_soma_tsy_get_asof():
    assert isinstance(soma.tsy_get_asof(date="2023-01-01"), pandas.DataFrame)


def test_soma_tsy_get_cusip():
    assert isinstance(soma.tsy_get_cusip(cusip="9127963K3"), pandas.DataFrame)


def test_soma_tsy_get_holdingtype_asof():
    assert isinstance(soma.tsy_get_holdingtype_asof(holding_type="all", date="2023-01-01"), pandas.DataFrame)


def test_soma_tsy_wam_holdingtype_asof():
    assert isinstance(soma.tsy_wam_holdingtype_asof(holding_type="all", date="2023-01-01"), pandas.DataFrame)


def test_soma_tsy_get_monthly():
    assert isinstance(soma.tsy_get_monthly(), pandas.DataFrame)


# Treasury Securities Operations
def test_tsy_latest():
    assert isinstance(tsy.latest(operation="all", status="results", include="summary"), pandas.DataFrame)


def test_tsy_results_last_two_weeks():
    assert isinstance(tsy.results_last_two_weeks(operation="all", include="summary"), pandas.DataFrame)


def test_tsy_results_last_number():
    assert isinstance(tsy.results_last_number(operation="all", include="summary", number=5), pandas.DataFrame)


def test_tsy_results_search():
    assert isinstance(tsy.results_search(operation="all", include="summary", start_date="2023-01-01"), pandas.DataFrame)
