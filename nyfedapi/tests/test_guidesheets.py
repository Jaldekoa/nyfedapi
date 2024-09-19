from nyfedapi import guidesheets
import pandas as pd
import pytest

@pytest.mark.skip
def test_guidesheets_latest():
    assert isinstance(guidesheets.latest(guidesheet_type="si"), pd.DataFrame)
    assert isinstance(guidesheets.latest(guidesheet_type="wi"), pd.DataFrame)
    assert isinstance(guidesheets.latest(guidesheet_type="fs"), pd.DataFrame)


@pytest.mark.skip
def test_guidesheets_previous():
    assert isinstance(guidesheets.previous(guidesheet_type="si"), pd.DataFrame)
    assert isinstance(guidesheets.previous(guidesheet_type="wi"), pd.DataFrame)
    assert isinstance(guidesheets.previous(guidesheet_type="fs"), pd.DataFrame)
