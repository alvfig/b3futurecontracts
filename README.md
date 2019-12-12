# b3futurecontracts

B3 is a stock exchange in Sao Paulo, Brazil. This module evaluates the rollover date of some of its future contracts.

## Classes

Currently this module provides two classes, `B3FutureIndex` and `B3FutureDollar`. These classes have two main methods, `rollover_date` and `current_name`; both take a date as argument and return the rollover date and the current names of the future contract as of the given date, respectively.

## Sample code

```python
>>> import datetime as dt
>>> from b3futurecontracts import *
>>>
>>> today = dt.date.today()
>>> print(today)
2019-12-01
>>>
>>> futureindex = B3FutureIndex(today)
>>> print(futureindex.rollover_date(), futureindex.current_name()[0])
2019-12-11 WINZ19
>>>
```

```shell
$ python -m b3futurecontracts
2019-01-05  2019-02-13 WING19  2019-02-01 WDOG19
2019-01-20  2019-02-13 WING19  2019-02-01 WDOG19
2019-02-05  2019-02-13 WING19  2019-03-01 WDOH19
2019-02-20  2019-04-17 WINJ19  2019-03-01 WDOH19
2019-03-05  2019-04-17 WINJ19  2019-04-01 WDOJ19
2019-03-20  2019-04-17 WINJ19  2019-04-01 WDOJ19
2019-04-05  2019-04-17 WINJ19  2019-05-02 WDOK19
2019-04-20  2019-06-12 WINM19  2019-05-02 WDOK19
2019-05-05  2019-06-12 WINM19  2019-06-03 WDOM19
2019-05-20  2019-06-12 WINM19  2019-06-03 WDOM19
2019-06-05  2019-06-12 WINM19  2019-07-01 WDON19
2019-06-20  2019-08-14 WINQ19  2019-07-01 WDON19
2019-07-05  2019-08-14 WINQ19  2019-08-01 WDOQ19
2019-07-20  2019-08-14 WINQ19  2019-08-01 WDOQ19
2019-08-05  2019-08-14 WINQ19  2019-09-02 WDOU19
2019-08-20  2019-10-16 WINV19  2019-09-02 WDOU19
2019-09-05  2019-10-16 WINV19  2019-10-01 WDOV19
2019-09-20  2019-10-16 WINV19  2019-10-01 WDOV19
2019-10-05  2019-10-16 WINV19  2019-11-01 WDOX19
2019-10-20  2019-12-18 WINZ19  2019-11-01 WDOX19
2019-11-05  2019-12-18 WINZ19  2019-12-02 WDOZ19
2019-11-20  2019-12-18 WINZ19  2019-12-02 WDOZ19
2019-12-05  2019-12-18 WINZ19  2020-01-02 WDOF20
2019-12-20  2020-02-12 WING20  2020-01-02 WDOF20
$
```

## Installation
```shell
pip install b3futurecontracts
```
