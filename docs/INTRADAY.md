## Trade Format

```javascript
trade = {
    order: 1, // used for ordering
    t: 91254, // time of trade
    p: 123, // price of trade
    v: 123, // volume of trade
}
```

## Snapshot Format

```javascript
snapshot = {
    t: 93503, // time in 
    lst: 123, // last trade price
    y: 123, // yesterdays price
    c: 123, // close price
    o: 123, // open price,
    h: 123, // high price,
    l: 123, // low price,
    cnt: 123, // trades count in that day until the snapshot
    v: 123, // traded volume until snapshot in that day
    s: 'A ', // state
    buy: [ // top 3 buy orders (may contain less than 3)
        {
            t: 85512, // time of the order
            cnt: 123, // number of participants in this price buy orders
            v: 123, // volume of buy orders
            p: 123, // price of buy orders
        },
        ...
    ],
    sell: [ // top 3 sell orders (may contain less than 3)
        {
            t: 85512, // time of the order
            cnt: 123, // number of participants in this price sell orders
            v: 123, // volume of sell orders
            p: 123, // price of sell orders
        },
        ...
    ]
}
```
