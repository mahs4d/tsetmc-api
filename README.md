# TSETMC Api

simple python library to extract data from [tsetmc](https://tsetmc.com).

## Usage

first install library using pip:

```shell script
pip3 install tsetmc-api
```

### Getting Daily Price Ticks of Asset

```python
import tsetmc_api

daily_ticks = tsetmc_api.get_daily_history('778253364357513')
```

you can find asset_id of any stock from it's webpage url in tsetmc (the i query).

### Getting Client Type History of Asset

```python
import tsetmc_api

client_type_history = tsetmc_api.get_client_type_history('778253364357513')
```
