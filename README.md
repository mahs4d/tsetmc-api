# TSETMC-API

This library is for getting data from [tsetmc](http://tsetmc.com) website. It is divided into 5 subcomponents:

## Installation

You can install this library using the following command:

`pip install tsetmc-api`

## Examples

You can find examples of using each component in `examples` directory.

| Component    | Example File                                                |
|--------------|-------------------------------------------------------------|
| Symbol       | [symbol_example.py](examples/symbol_example.py)             |
| Market Watch | [market_watch_example.py](examples/market_watch_example.py) |
| Day Details  | [day_details_example.py](examples/day_details_example.py)   |
| Market Map   | [market_map_example.py](examples/market_map_example.py)     |
| Group        | [group_example.py](examples/group_example.py)               |

## Usage

- **symbol:** working with main symbol page and live data (
  e.g. [this page](http://www.tsetmc.com/loader.aspx?ParTree=151311&i=43362635835198978))
- **market_watch:** getting data visible from [market watch page](http://www.tsetmc.com/Loader.aspx?ParTree=15131F)
- **day_details:** working with details of a symbol in a single day of history (
  e.g. [this page](http://cdn.tsetmc.com/History/43362635835198978/20221029))
- **market_map:** getting data visible in [market map page](http://main.tsetmc.com/marketmap)
- **group:** getting list of available symbol groups

### Symbol Component (tsetmc_api.symbol)

![Symbol Component](https://github.com/mahs4d/tsetmc-api/blob/master/docs/images/Symbol.png?raw=true)

### Market Watch Component (tsetmc_api.market_watch)

![Market Watch Component](https://github.com/mahs4d/tsetmc-api/blob/master/docs/images/MarketWatch.png?raw=true)

### Day Details Component (tsetmc_api.day_details)

![Day Details Component](https://github.com/mahs4d/tsetmc-api/blob/master/docs/images/DayDetails.png?raw=true)

### Market Map Component (tsetmc_api.market_map)

![Market Map Component](https://github.com/mahs4d/tsetmc-api/blob/master/docs/images/MarketMap.png?raw=true)

### Group Component (tsetmc_api.group)

Group component currently only has one function (`get_all_groups`) which returns all the symbol groups.

### Errors

Tsetmc sometimes returns 403 and you should retry.

### TODO

- [ ] Migrate `symbol` component to use new tsetmc.
- [ ] Migrate `market_watch` component to use new tsetmc.
- [x] Migrate `day_details` component to use new tsetmc.
- [x] Migrate `market_map` component to use new tsetmc.
- [x] Migrate `group` component to use new tsetmc.
- [ ] Support asyncio.

## Support and Donation

If this repository helped you, please support it by giving a star (:star:).

For contacting me about this project please use the following email:

[mahdi74sadeghi+tsetmc_api@gmail.com](mailto:mahdi74sadeghi+tsetmc_api@gmail.com)
