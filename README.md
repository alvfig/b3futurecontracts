# b3futurecontracts

B3 is a stock exchange in Sao Paulo, Brazil. This module evaluates the rollover date of some of its future contracts.

## Classes

Currently this module provides two classes, `B3FutureIndex` and `B3FutureDollar`. The classes have two main methods, `rollover_date` and `current_name`; both take a date as argument and return the rollover date and the current name of the future contract as of the given date, respectively.

## Sample code

```python
import datetime as dt
from b3futurecontracts import *

today = dt.date.today()
print(today)

futureindex = B3FutureIndex(today)
print(futureindex.rollover_date(), futureindex.current_name()[0])
```

```shell
python -m b3futurecontracts
```

## Install
```shell
pip install b3futurecontracts
```
