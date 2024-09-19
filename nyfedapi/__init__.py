from urllib.parse import urlencode
import pandas

__all__ = ["ambs", "fxs", "guidesheets", "pd", "marketshare", "rates", "rp", "seclending", "soma", "tsy"]


def __get_data(endpoint: str, **kwargs) -> pandas.DataFrame:
    if not kwargs:
        return pandas.read_csv(f"https://markets.newyorkfed.org{endpoint}")
    else:
        return pandas.read_csv(f"https://markets.newyorkfed.org{endpoint}?{urlencode(kwargs)}")
