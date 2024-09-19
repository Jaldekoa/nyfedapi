from urllib.parse import urlencode
import pandas as pd

__all__ = ["ambs", "fxs", "guidesheets", "pd", "marketshare", "rates", "rp", "seclending", "soma", "tsy"]


def __get_data(endpoint: str, **kwargs) -> pd.DataFrame:
    if not kwargs:
        return pd.read_csv(f"https://markets.newyorkfed.org{endpoint}")
    else:
        return pd.read_csv(f"https://markets.newyorkfed.org{endpoint}?{urlencode(kwargs)}")
