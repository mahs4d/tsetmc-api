# TSETMC Api

simple python library to extract data from [tsetmc](https://tsetmc.com).

## Usage

first install library using pip:

```shell script
pip3 install tsetmc-api
```

after that in your code:

```python
import tsetmc_api

daily_ticks = tsetmc_api.get_daily_history('778253364357513')
```

you can find symbol_i of any stock from it's webpage url in tsetmc (the i query).
