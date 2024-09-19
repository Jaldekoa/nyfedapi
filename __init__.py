from urllib.parse import urlencode
import pandas as pd

__base_url = "https://markets.newyorkfed.org"
__all__ = ["ambs", "fxs", "guidesheets", "pd", "marketshare", "rates", "rp", "seclending", "soma", "tsy"]


# TODO: Implement valid parameters and values in all FRBoNY
def __valid_params(params: dict, valid_params: dict):
    return {k: params[k] for k, v in valid_params.items() if params[k] in v}


def __read_csv_with_kwargs(url: str, kwargs: dict) -> pd.DataFrame:
    all_url = f"{url}?{urlencode(kwargs)}"
    return pd.read_csv(all_url)
