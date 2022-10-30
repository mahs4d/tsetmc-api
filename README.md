# TSETMC-API

This library is for getting data from [tsetmc](http://tsetmc.com) website. It is divided into 5 subcomponents:

## Installation

You can install this library using the following command:

`pip install tsetmc-api`

## Usage

- **symbol:** working with main symbol page and live data (e.g. [this page](http://www.tsetmc.com/loader.aspx?ParTree=151311&i=43362635835198978))
- **market_watch:** getting data visible from [market watch page](http://www.tsetmc.com/Loader.aspx?ParTree=15131F)
- **day_details:** working with details of a symbol in a single day of history (e.g. [this page](http://cdn.tsetmc.com/History/43362635835198978/20221029))
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

## Support and Donation
If this repository helped you, please support it by giving a star (:star:).
For donation please contact me at [mahdi74sadeghi@gmail.com](mailto:mahdi74sadeghi@gmail.com).
