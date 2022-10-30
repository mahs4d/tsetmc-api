# TSETMC-API

This library is for getting data from [tsetmc](http://tsetmc.com) website. It is divided into 5 subcomponents:

- **symbol:** working with main symbol page and live data (e.g. [this page](http://www.tsetmc.com/loader.aspx?ParTree=151311&i=43362635835198978))
- **market_watch:** getting data visible from [market watch page](http://www.tsetmc.com/Loader.aspx?ParTree=15131F)
- **day_details:** working with details of a symbol in a single day of history (e.g. [this page](http://cdn.tsetmc.com/History/43362635835198978/20221029))
- **market_map:** getting data visible in [market map page](http://main.tsetmc.com/marketmap)
- **group:** getting list of available symbol groups

## Symbol Component (tsetmc_api.symbol)

![Symbol Component](/docs/images/Symbol.drawio)

## Market Watch Component (tsetmc_api.market_watch)

![Market Watch Component](/docs/images/MarketWatch.drawio)

## Day Details Component (tsetmc_api.day_details)

![Day Details Component](/docs/images/DayDetails.drawio)

## Market Map Component (tsetmc_api.market_map)

![Market Map Component](/docs/images/MarketMap.drawio)

## Group Component (tsetmc_api.group)

Group component currently only has one function (`get_all_groups`) which returns all the symbol groups.

# Support and Donate
If this repository helped you can support it by giving a :star: and donating using one of the following links:

