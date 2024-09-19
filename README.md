# nyfedapi
This repository contains a Python wrapper to easily retrieve data from the Federal Reserve Bank of New York (FRBoNY) official API in pandas format.

## Overview
The Markets Data APIs are provided to external users and applications to request data from the Federal Reserve Bank of New York. FRBoNY's API does not require tokens or registration, so feel free to use it immediately.

There are ten databases with their endpoints that the FRBoNY has exposed to the public:

- Agency Mortgage-Backed Securities Operations
- Central Bank Liquidity Swaps Operations
- Guide Sheets
- Primary Dealer Statistics
- Primary Dealer Statistics Market Share
- Reference Rates
- Repo and Reverse Repo Operations
- Securities Lending Operations
- System Open Market Account Holdings
- Treasury Securities Operations

## Requirements
- Python 3.9 or higher.
- Requests
- Pandas

## Installation
```terminal
pip install nyfedapi
```

## Agency Mortage-Backed Securities Operations

### ambs.latest
Returns the latest AMBS operation Announcements or Results for the current day.

```python
from nyfedapi import ambs
df = ambs.latest(operation, status, include)
```

#### Parameters
| Parameter   | Type  | Description                                                                         |
|-------------|-------|-------------------------------------------------------------------------------------|
| `operation` | `str` | The operation type. Available values: ["all", "purchases", "sales", "roll", "swap"] |
| `status`    | `str` | The operation status. Available values: ["announcements", "results"]                |
| `include`   | `str` | The level of details to include. Available values: ["summary", "details"]           |

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest AMBS operation announcements or results for the current day.


### ambs.results_last_two_weeks
Returns the last two weeks AMBS operations Results.

```python
from nyfedapi import ambs
df = ambs.results_last_two_weeks(operation, include)
```

#### Parameters
| Parameter   | Type  | Description                                                                         |
|-------------|-------|-------------------------------------------------------------------------------------|
| `operation` | `str` | The operation type. Available values: ["all", "purchases", "sales", "roll", "swap"] |
| `include`   | `str` | The level of details to include. Available values: ["summary", "details"]           |

#### Returns
- `pd.DataFrame`: A DataFrame containing the last two weeks AMBS operations results.


### ambs.results_last_number
Returns the last N number of AMBS operations Results.

```python
from nyfedapi import ambs
df = ambs.results_last_two_weeks(operation, include, number)
```

#### Parameters
| Parameter   | Type  | Description                                                                         |
|-------------|-------|-------------------------------------------------------------------------------------|
| `operation` | `str` | The operation type. Available values: ["all", "purchases", "sales", "roll", "swap"] |
| `include`   | `str` | The level of details to include. Available values: ["summary", "details"]           |
| `number`    | `int` | The last N amount of operations to return.                                          |

#### Returns
- `pd.DataFrame`: A DataFrame containing the last N number of AMBS operations results.


### ambs.results_search
Returns AMBS operations Results.

```python
from nyfedapi import ambs
df = ambs.results_search(operation, include, **kwargs)
```

#### Parameters
| Parameter    | Type  | Description                                                                                                                  |
|--------------|-------|------------------------------------------------------------------------------------------------------------------------------|
| `operation`  | `str` | The operation type. Available values: ["all", "purchases", "sales", "roll", "swap"]                                          |
| `include`    | `str` | The level of details to include. Available values: ["summary", "details"]                                                    |
| `start_date` | `str` | The start date (inclusive) from which to search. Format YYYY-MM-DD.                                                          |
| `end_date`   | `str` | The end date (inclusive) up until which to search. Format YYYY-MM-DD.                                                        |
| `securities` | `str` | Filter by securities (Operation Method). Available values: ["Basket", "Coupon Swap", "Dollar Roll", "Specified Pool", "TBA"] |
| `cusip`      | `str` | Only return operations which include the given CUSIP. Partial identifiers are accepted.                                      |
| `desc`       | `str` | Only return operations which include the given Security Description. Partial identifiers are accepted.                       |


#### Returns
- `pd.DataFrame`: A DataFrame containing the AMBS operations results.


## Central Bank Liquidity Swaps Operations

### fxs.latest
Returns the latest Liquidity Swaps operation Results posted on current day.

```python
from nyfedapi import fxs
df = fxs.latest(operation_type)
```

#### Parameters
| Parameter        | Type  | Description                                                                              |
|------------------|-------|------------------------------------------------------------------------------------------|
| `operation_type` | `str` | The operation type to search for. Available values: ["all", "usdollar", "nonusdollar"]   |

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest Liquidity Swaps operation results posted on current day.


### fxs.last_number
Returns the last N number of Liquidity Swaps operations Results.

```python
from nyfedapi import fxs
df = fxs.last_number(operation_type, number)
```

#### Parameters
| Parameter        | Type  | Description                                                                            |
|------------------|-------|----------------------------------------------------------------------------------------|
| `operation_type` | `str` | The operation type to search for. Available values: ["all", "usdollar", "nonusdollar"] |
| `number`         | `int` | The last N amount of trades to return                                                  |

#### Returns
- `pd.DataFrame`: A DataFrame containing the last N number of Liquidity Swaps operations results.


### fxs.search
Returns Liquidity Swaps operation Results.

```python
from nyfedapi import fxs
df = fxs.search(operation_type, **kwargs)
```

#### Parameters
| Parameter        | Type  | Description                                                                            |
|------------------|-------|----------------------------------------------------------------------------------------|
| `operation_type` | `str` | The operation type to search for. Available values: ["all", "usdollar", "nonusdollar"] |
| `start_date`     | `str` | The start date (inclusive) from which to search, depending on date type. Defaults to current date. Format YYYY-MM-DD. |
| `end_date`       | `str` | The end date (inclusive) up until which to search, depending on date type.  Format YYYY-MM-DD. |
| `date_type`      | `str` | The date type to search for within the start and end. Defaults to trade date. Available values : ["trade", "maturity"] |
| `counterparties` | `str` | A comma-separated list of counterparty names to search for. Partial names are accepted. |

#### Returns
- `pd.DataFrame`: A DataFrame containing Liquidity Swaps operation Results.


### fxs.counterparties
Returns Counterparties of Liquidity Swaps operations.

```python
from nyfedapi import fxs
df = fxs.counterparties()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing counterparties of Liquidity Swaps operations.


## Guide Sheets

### guidesheets.latest
Returns the latest Guide Sheet. Work in Progress (WIP).

```python
from nyfedapi import guidesheets
df = guidesheets.latest()
```

#### Parameters
| Parameter        | Type  | Description                                                |
|------------------|-------|------------------------------------------------------------|
| `guidesheet_type` | `str` | The guide sheet type. Available values: ["si", "wi", "fs"] |

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest Guide Sheet.


### guidesheets.previous
Returns the previous Guide Sheet. Work in Progress (WIP).

```python
from nyfedapi import guidesheets
df = guidesheets.previous()
```

#### Parameters
| Parameter        | Type  | Description                                                |
|------------------|-------|------------------------------------------------------------|
| `guidesheet_type` | `str` | The guide sheet type. Available values: ["si", "wi", "fs"] |

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest Guide Sheet.


## Primary Dealer Statistics

### pd.latest
Returns the latest Survey results for each timeseries.

```python
from nyfedapi import pd
df = pd.latest()
```

#### Parameters
| Parameter     | Type  | Description                 |
|---------------|-------|-----------------------------|
| `seriesbreak` | `str` | A valid series break value. |

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest Survey results for each timeseries.


### pd.get_all_timeseries
Returns all Survey results.

```python
from nyfedapi import pd
df = pd.get_all_timeseries()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing all Survey results.


### pd.list_timeseries
Returns Description of timeseries/keyids.

```python
from nyfedapi import pd
df = pd.list_timeseries()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing description of timeseries/keyids.


### pd.list_asof
Returns all As Of Dates with respective Series Break.

```python
from nyfedapi import pd
df = pd.list_asof()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing all as of dates with respective series break.


### pd.list_seriesbreaks
Returns Series Breaks including Label, Start and End Date.

```python
from nyfedapi import pd
df = pd.list_seriesbreaks()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing series breaks including label, start and end date.


### pd.get_asof
Returns single date Survey results.

```python
from nyfedapi import pd
df = pd.get_asof()
```

#### Parameters
| Parameter | Type  | Description                                    |
|-----------|-------|------------------------------------------------|
| `date`    | `str` | The time series as of date. Format YYYY-MM-DD. |

#### Returns
- `pd.DataFrame`: A DataFrame containing single date survey results.


### pd.get_timeseries
Return Survey results for given timeseries across all Series Breaks. To query multiple timeseries, separate each with underscore(_).

```python
from nyfedapi import pd
df = pd.get_timeseries()
```

#### Parameters
| Parameter    | Type  | Description                                         |
|--------------|-------|-----------------------------------------------------|
| `timeseries` | `str` | A list of time series ids separated by underscores. |

#### Returns
- `pd.DataFrame`: A DataFrame containing survey results for given timeseries across all series breaks.


### pd.get_seriesbreaks_timeseries
Return Survey results for given timeseries across all Series Breaks. To query multiple timeseries, separate each with underscore(_).

```python
from nyfedapi import pd
df = pd.get_seriesbreaks_timeseries()
```

#### Parameters
| Parameter      | Type  | Description                                         |
|----------------|-------|-----------------------------------------------------|
| `seriesbreaks` | `str` | A valid series break value. |
| `timeseries`   | `str` | A list of valid time series separated with underscores. |

#### Returns
- `pd.DataFrame`: A DataFrame containing survey results for given timeseries across all series breaks.


## Primary Dealer Statistics Market Share

### marketshare.qtrly_latest
Returns the latest quarterly Market Share.

```python
from nyfedapi import marketshare
df = marketshare.qtrly_latest()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest quarterly market share.


### marketshare.ytd_latest

Returns the latest year-to-date Market Share.

```python
from nyfedapi import marketshare
df = marketshare.ytd_latest()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest year-to-date market share.


## Reference Rates

### rates.all_latest
Returns the latest secured and unsecured rates.

```python
from nyfedapi import rates
df = rates.all_latest()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest secured and unsecured rates.


### rates.all_search
Returns the latest secured and unsecured rates.

```python
from nyfedapi import rates
df = rates.all_search()
```

#### Parameters
| Parameter    | Type  | Description                                                                                       |
|--------------|-------|---------------------------------------------------------------------------------------------------|
| `start_date` | `str` | The start date (inclusive) from which to search. Defaults to the current date. Format YYYY-MM-DD. |
| `end_date`   | `str` | The end date (inclusive) up until which to search. Format YYYY-MM-DD.                             |
| `type`       | `str` | The report type to return. Available values : ["rate", "volume"]                                                                       |

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest secured and unsecured rates.


### rates.secured_all_latest
Returns the latest secured rates.

```python
from nyfedapi import rates
df = rates.secured_all_latest()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest secured rates.


### rates.secured_last_number
Returns the last N number of secured rates.

```python
from nyfedapi import rates
df = rates.secured_last_number(rate_type, number)
```

#### Parameters
| Parameter   | Type  | Description                                                          |
|-------------|-------|----------------------------------------------------------------------|
| `rate_type` | `str` | The rate type. Available values : ["tgcr", "bgcr", "sofr", "sofrai"] |
| `number`    | `int` | The last N amount of rates to return.                                |

#### Returns
- `pd.DataFrame`: A DataFrame containing the last N number of secured rates.


### rates.secured_search
Returns secured rates and/or volume.

```python
from nyfedapi import rates
df = rates.secured_search(rate_type, **kwargs)
```

#### Parameters
| Parameter    | Type  | Description                                                                                      |
|--------------|-------|--------------------------------------------------------------------------------------------------|
| `rate_type`  | `str` | The rate type. Available values : ["all", "tgcr", "bgcr", "sofr", "sofrai"]                      |
| `start_date` | `str` | The start date (inclusive) from which to search. Defaults to the current date. Format YYYY-MM-DD |
| `end_date`   | `str` | The end date (inclusive) up until which to search. Format YYYY-MM-DD                             |
| `type`  | `str` | The report type to return. Available values : ["rate", "volume"]                                 |

#### Returns
- `pd.DataFrame`: A DataFrame containing secured rates and/or volume.


### rates.unsecured_all_latest
Returns the latest unsecured rates.

```python
from nyfedapi import rates
df = rates.unsecured_all_latest()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest unsecured rates.


### rates.unsecured_last_number
Returns the last N number of unsecured rates.

```python
from nyfedapi import rates
df = rates.unsecured_last_number(rate_type, number)
```

#### Parameters
| Parameter   | Type  | Description                                         |
|-------------|-------|-----------------------------------------------------|
| `rate_type` | `str` | The rate type. Available values : ["effr", "obfr"]  |
| `number`    | `int` | The last N amount of rates to return.               |

#### Returns
- `pd.DataFrame`: A DataFrame containing the last N number of unsecured rates.


### rates.unsecured_search
Returns unsecured rates and/or volume.

```python
from nyfedapi import rates
df = rates.unsecured_search(rate_type, **kwargs)
```

#### Parameters
| Parameter    | Type  | Description                                                                                       |
|--------------|-------|---------------------------------------------------------------------------------------------------|
| `rate_type`  | `str` | The rate type. Available values : ["all", "efr", "obfr"]                                          |
| `start_date` | `str` | The start date (inclusive) from which to search. Defaults to the current date. Format YYYY-MM-DD. |
| `end_date`   | `str` | The end date (inclusive) up until which to search. Format YYYY-MM-DD.                             |
| `type`  | `str` | The report type to return. Available values : ["rate", "volume"]                                  |

#### Returns
- `pd.DataFrame`: A DataFrame containing unsecured rates and/or volume.


## Repo and Reverse Repo Operations

### rp.latest
Returns the latest Repo and/or Reverse Repo operations Announcements or Results for the current day.

```python
from nyfedapi import rp
df = rp.latest(operation_type, method, status)
```

#### Parameters
| Parameter        | Type  | Description                                                                     |
|------------------|-------|---------------------------------------------------------------------------------|
| `operation_type` | `str` | The operation type. Available values : ["all", "repo", "reverserepo"]           |
| `method`         | `str` | The operation method. Available values : ["all", "fixed", "single", "multiple"] |
| `status`         | `str` | The operation status. Available values : ["announcements", "results"]           |

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest repo and/or reverse repo operations announcements or results for the current day.


### rp.results_last_two_weeks
Returns the last two weeks Repo and/or Reverse Repo operations Results.

```python
from nyfedapi import rp
df = rp.results_last_two_weeks(operation_type, method)
```

#### Parameters
| Parameter        | Type  | Description                                                                     |
|------------------|-------|---------------------------------------------------------------------------------|
| `operation_type` | `str` | The operation type. Available values : ["all", "repo", "reverserepo"]           |
| `method`         | `str` | The operation method. Available values : ["all", "fixed", "single", "multiple"] |

#### Returns
- `pd.DataFrame`: A DataFrame containing the last two weeks repo and/or reverse repo operations results.


### rp.results_last_number
Returns the last N number of Repo and/or Reverse Repo operations Results.

```python
from nyfedapi import rp
df = rp.results_last_number(operation_type, method, number)
```

#### Parameters
| Parameter        | Type  | Description                                                                    |
|------------------|-------|--------------------------------------------------------------------------------|
| `operation_type` | `str` | The operation type. Available values : ["all", "repo", "reverserepo"]          |
| `method`         | `str` | The operation method. Available values : ["all", "fixed", "single", "multiple"] |
| `number`         | `int` | The last N amount of operations to return. |

#### Returns
- `pd.DataFrame`: A DataFrame containing the last N number of repo and/or reverse repo operations results.


### rp.results_search
Returns Repo and/or Reverse Repo operation Results.

```python
from nyfedapi import rp
df = rp.results_search(**kwargs)
```

#### Parameters
| Parameter         | Type  | Description                                                                                                                                                                      |
|-------------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `start_date`      | `str` | The start date (inclusive) from which to search. Format YYYY-MM-DD.                                                                                                              |
| `end_date`        | `str` | The end date (inclusive) up until which to search. Format YYYY-MM-DD.                                                                                                            |
| `operation_types` | `str` | The operation types (comma-delimited) by which to filter. Available values : ["Repo", "Reverse Repo"]                                                                                  |
| `method`          | `str` | The operation method by which to filter. Available values : ["multiple", "single", "fixed"]                                                                                      |
| `security_type`   | `str` | The security type (tranche) by which to filter. For specific types, only operations which include that type will be returned. Available values : ["mbs", "agency", "tsy", "srf"] |
| `term`            | `str` | The term of the operation. Available values : ["overnight", "term"]                                                                                                              |

#### Returns
- `pd.DataFrame`: A DataFrame containing repo and/or reverse repo operation results.


### rp.reverserepo_propositions_search
Returns Propositions for Reverse Repo operations.

```python
from nyfedapi import rp
df = rp.reverserepo_propositions_search(**kwargs)
```

#### Parameters
| Parameter         | Type  | Description                                                                                                                                                                      |
|-------------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `start_date`      | `str` | The start date (inclusive) from which to search. Format YYYY-MM-DD.                                                                                                              |
| `end_date`        | `str` | The end date (inclusive) up until which to search. Format YYYY-MM-DD.                                                                                                            |

#### Returns
- `pd.DataFrame`: A DataFrame containing propositions for reverse repo operations.


## Securities Lending Operations

### seclending.results_latest
Returns the latest Securities Lending operation Results for the current day.

```python
from nyfedapi import seclending
df = seclending.results_latest(operation, include)
```

#### Parameters
| Parameter   | Type  | Description                                                                                                                                                                      |
|-------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operation` | `str` | The operation type. Available values : ["all", "seclending", "extensions"].                                                                                                              |
| `include`   | `str` | The level of details to include. Available values : ["summary", "details"].                                                                                                            |

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest securities lending operation results for the current day.


### seclending.results_last_two_weeks
Returns the last two weeks Securities Lending operation Results and/or Extensions.

```python
from nyfedapi import seclending
df = seclending.results_last_two_weeks(operation, include)
```

#### Parameters
| Parameter   | Type  | Description                                                                                                                                                                      |
|-------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operation` | `str` | The operation type. Available values : ["all", "seclending", "extensions"].                                                                                                              |
| `include`   | `str` | The level of details to include. Available values : ["summary", "details"].                                                                                                            |

#### Returns
- `pd.DataFrame`: A DataFrame containing the last two weeks securities lending operation results and/or extensions.


### seclending.results_last_number
Returns the last N number of Securities Lending operation Results and/or Extensions.

```python
from nyfedapi import seclending
df = seclending.results_last_number(operation, include, number)
```

#### Parameters
| Parameter   | Type  | Description                                                                                                                                                                      |
|-------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operation` | `str` | The operation type. Available values : ["all", "seclending", "extensions"].                                                                                                              |
| `include`   | `str` | The level of details to include. Available values : ["summary", "details"].                                                                                                            |
| `number`    | `int` | The last N amount of operations to return.                                                                                                            |

#### Returns
- `pd.DataFrame`: A DataFrame containing the last N number of securities lending operation results and/or extensions.


### seclending.results_search
Returns Securities Lending operation Results and/or Extensions.

```python
from nyfedapi import seclending
df = seclending.results_search(operation, include)
```

#### Parameters
| Parameter   | Type  | Description                                                                                                                                                                      |
|-------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operation` | `str` | The operation type. Available values : ["all", "seclending", "extensions"].                                                                                                              |
| `include`   | `str` | The level of details to include. Available values : ["summary", "details"].                                                                                                            |

#### Returns
- `pd.DataFrame`: A DataFrame containing securities lending operation results and/or extensions.


## System Open Market Account Holdings

### soma.asofdates_latest
Returns the latest SOMA holdings As Of Date.

```python
from nyfedapi import soma
df = soma.asofdates_latest()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest SOMA holdings As Of Date.


### soma.summary
Returns Summary Of SOMA holdings for each As of Date and holding type.

```python
from nyfedapi import soma
ndf = soma.summary()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing summary of SOMA holdings for each as of date and holding type.


### soma.asofdates_list
Returns all SOMA holdings As of Date.

```python
from nyfedapi import soma
df = soma.asofdates_list()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing all SOMA holdings as of date.


### soma.agency_get_release_log
Returns the last three months Agency Release and As Of Dates.

```python
from nyfedapi import soma
df = soma.agency_get_release_log()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing the last three months Agency release and as of dates.


### soma.agency_get_asof
Returns a single date SOMA Agency Holdings.

```python
from nyfedapi import soma
df = soma.agency_get_asof(date)
```

#### Parameters
| Parameter | Type  | Description                                                                 |
|-----------|-------|-----------------------------------------------------------------------------|
| `date`    | `str` | The date for which to retrieve the agency release. Format YYYY-MM-DD.       |

#### Returns
- `pd.DataFrame`: A DataFrame containing a single date SOMA Agency holdings.


### soma.agency_get_cusip
Returns all SOMA Agency Holdings for a single CUSIP.

```python
from nyfedapi import soma
df = soma.agency_get_cusip(cusip)
```

#### Parameters
| Parameter | Type  | Description                                                                 |
|----------|-------|-----------------------------------------------------------------------------|
| `cusip`  | `str` | The CUSIP for which to retrieve information.       |

#### Returns
- `pd.DataFrame`: A DataFrame containing all SOMA Agency Holdings for a single CUSIP.


### soma.agency_get_holdingtype_asof
Returns a single date SOMA Agency Holdings for a Agency holding type.

```python
from nyfedapi import soma
df = soma.agency_get_holdingtype_asof(holding_type, date)
```

#### Parameters
| Parameter      | Type  | Description                                                                                     |
|----------------|-------|-------------------------------------------------------------------------------------------------|
| `holding_type` | `str` | The holding type for which to retrieve. Available values: ["all", "agency debts", "mbs", "cmb"] |
| `date`         | `str` | The date for which to retrieve the agency release. Format YYYY-MM-DD.                           |

#### Returns
- `pd.DataFrame`: A DataFrame containing a single date SOMA Agency holdings for a Agency holding type.


### soma.agency_wam_asof
Returns a single date Weighted Average Maturity for Agency Debt.

```python
from nyfedapi import soma
df = soma.agency_wam_asof(date)
```

#### Parameters
| Parameter      | Type  | Description                                                                                     |
|----------------|-------|-------------------------------------------------------------------------------------------------|
| `date`         | `str` | The date for which to retrieve the Weighted Average Maturity number. Format YYYY-MM-DD.                           |

#### Returns
- `pd.DataFrame`: A DataFrame containing a single date Weighted Average Maturity for Agency Debt.


### soma.tsy_get_release_log
Returns the last three months Treasury Release and As Of Dates.

```python
from nyfedapi import soma
df = soma.tsy_get_release_log()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing the last three months Treasury release and as of dates.


### soma.tsy_get_asof
Returns a single date SOMA Treasury Holdings.

```python
from nyfedapi import soma
df = soma.tsy_get_asof(date)
```

#### Parameters
| Parameter | Type  | Description                                                             |
|-----------|-------|-------------------------------------------------------------------------|
| `date`    | `str` | The date for which to retrieve the treasury release. Format YYYY-MM-DD. |

#### Returns
- `pd.DataFrame`: A DataFrame containing a single date SOMA Treasury holdings.


### soma.tsy_get_cusip
Returns all SOMA Treasury Holdings for a single CUSIP.

```python
from nyfedapi import soma
df = soma.tsy_get_cusip(cusip)
```

#### Parameters
| Parameter | Type  | Description                                                                 |
|----------|-------|-----------------------------------------------------------------------------|
| `cusip`  | `str` | The CUSIP for which to retrieve information.       |

#### Returns
- `pd.DataFrame`: A DataFrame containing all SOMA Treasury Holdings for a single CUSIP.


### soma.tsy_get_holdingtype_asof
Returns a single date SOMA Treasury Holdings for a Treasury holding type.

```python
from nyfedapi import soma
df = soma.tsy_get_holdingtype_asof(holding_type, date)
```

#### Parameters
| Parameter      | Type  | Description                                                                                             |
|----------------|-------|---------------------------------------------------------------------------------------------------------|
| `holding_type` | `str` | The holding type for which to retrieve. Available values: ["all", "bills", "notesbonds", "frn", "tips"] |
| `date`         | `str` | The date for which to retrieve the treasury release. Format YYYY-MM-DD.                                 |

#### Returns
- `pd.DataFrame`: A DataFrame containing a single date SOMA Treasury Holdings for a Treasury holding type.


### soma.tsy_wam_holdingtype_asof
Returns a single date Weighted Average Maturity for a Treasury holding type.

```python
from nyfedapi import soma
ndf = soma.tsy_wam_holdingtype_asof(holding_type, date)
```

#### Parameters
| Parameter      | Type  | Description                                                                                             |
|----------------|-------|---------------------------------------------------------------------------------------------------------|
| `holding_type` | `str` | The holding type for which to retrieve. Available values: ["all", "bills", "notesbonds", "frn", "tips"] |
| `date`         | `str` | The date for which to retrieve the Weighted Average Maturity number. Format YYYY-MM-DD.                 |

#### Returns
- `pd.DataFrame`: A DataFrame containing a single date Weighted Average Maturity for a Treasury holding type.


### soma.tsy_get_monthly
Returns all SOMA Treasury Holdings at monthly intervals.

```python
from nyfedapi import soma
df = soma.tsy_get_monthly()
```

#### Returns
- `pd.DataFrame`: A DataFrame containing all SOMA Treasury Holdings at monthly intervals.


## Treasury Securities Operations

### tsy.latest
Returns the latest Treasury operation Announcements or Results for the current day.

```python
from nyfedapi import tsy
df = tsy.latest(operation, status, include)
```

#### Parameters
| Parameter   | Type  | Description                                                                         |
|-------------|-------|-------------------------------------------------------------------------------------|
| `operation` | `str` | The operation type. Available values: ["all", "purchases", "sales"]                 |
| `status`    | `str` | The operation status. Available values: ["announcements", "results", "operations""] |
| `include`   | `str` | The level of details to include. Available values: ["summary", "details"]           |

#### Returns
- `pd.DataFrame`: A DataFrame containing the latest Treasury operation announcements or results for the current day.


### tsy.results_last_two_weeks
Returns the last two weeks Treasury operations Results.

```python
from nyfedapi import tsy
df = tsy.results_last_two_weeks(operation, include)
```

#### Parameters
| Parameter   | Type  | Description                                                                         |
|-------------|-------|-------------------------------------------------------------------------------------|
| `operation` | `str` | The operation type. Available values: ["all", "purchases", "sales"]                 |
| `include`   | `str` | The level of details to include. Available values: ["summary", "details"]           |

#### Returns
- `pd.DataFrame`: A DataFrame containing the last two weeks Treasury operations results.


### tsy.results_last_number
Returns the last N number of Treasury operations Results.

```python
from nyfedapi import tsy
df = tsy.results_last_number(operation, include, number)
```

#### Parameters
| Parameter   | Type  | Description                                                               |
|-------------|-------|---------------------------------------------------------------------------|
| `operation` | `str` | The operation type. Available values: ["all", "purchases", "sales"]       |
| `include`   | `str` | The level of details to include. Available values: ["summary", "details"] |
| `number`    | `int` | The last amount of results to return from current date.                   |

#### Returns
- `pd.DataFrame`: A DataFrame containing the last N number of Treasury operations Results.


### tsy.results_search
Returns Treasury operation Results.

```python
from nyfedapi import tsy
df = tsy.results_search(operation, include)
```

#### Parameters
| Parameter   | Type  | Description                                                               |
|-------------|-------|---------------------------------------------------------------------------|
| `operation` | `str` | The operation type. Available values: ["all", "purchases", "sales"]       |
| `include`   | `str` | The level of details to include. Available values: ["summary", "details"] |

#### Returns
- `pd.DataFrame`: A DataFrame containing Treasury operation results.


## TODO
- [ ] Add a keyword argument (kwargs) translator. Example: startDate -> start_date
- [ ] Implement the marketshare and guidesheets endpoints, as they currently do not support CSV format download.
- [ ]  Issue with ```seclending.results_search()```: Although startDate and endDate are not required, omitting them results in a 404 error with the response: ["Cannot exceed allowed span of 1 year"].
- [ ] Issue with ```ambs.results_search()```: Although startDate and endDate are not required, omitting them results in a 404 error with the response: ["Cannot exceed allowed span of 2 years"].

## API Documentation
- [Markets Data APIs: Federal Reserve Bank of New York (FRBoNY)](https://markets.newyorkfed.org/static/docs/markets-api.html)