from nyfedapi import marketshare
import pandas as pd
import pytest

@pytest.mark.skip
def test_marketshare_qtrly_latest():
    assert isinstance(marketshare.qtrly_latest(), pd.DataFrame)


@pytest.mark.skip
def test_marketshare_ytd_latest():
    assert isinstance(marketshare.ytd_latest(), pd.DataFrame)
