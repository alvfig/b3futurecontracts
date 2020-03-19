#!/usr/bin/python3
'''B3 is a stock exchange in Sao Paulo, Brazil. This module
evaluates the rollover date of some of its future contracts.'''

import datetime as dt

__all__ = ['B3FutureIndex', 'B3FutureDollar']


def easter(year):
    '''Evaluates the Easter day of year.'''

    if not isinstance(year, int):
        raise TypeError('year must be an integer')
    if year < 1582:
        raise ValueError('year must be greater than 1582')

    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19*a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2*e + 2*i - h - k) % 7
    m = (a + 11*h + 22*l) // 451
    month = (h + l - 7*m + 114) // 31
    day = (h + l - 7*m + 114) % 31 + 1

    return dt.date(year, month, day)


def holidays(year):
    '''Returns all holidays of year on Sao Paulo, Brazil'''

    holidays_ = [
        dt.date(year, 1, 1),    # New Year
        dt.date(year, 1, 25),   # Anniversary of SP
        dt.date(year, 5, 1),    # Day of the Work
        dt.date(year, 9, 7),    # Independence Day
        dt.date(year, 10, 12),  # Holy Mary's Day
        dt.date(year, 11, 2),   # Dead's Day
        dt.date(year, 11, 15),  # Day of the Republic
        dt.date(year, 11, 20),  # Black Conscience Day
        dt.date(year, 12, 25),  # Christmas
    ]

    # Easter
    easter_ = easter(year)
    holidays_.append(easter)

    # Carnival
    carnival = easter_ - dt.timedelta(days=47)
    holidays_.append(carnival)

    # Holy Friday
    holy_friday = easter_ - dt.timedelta(days=2)
    holidays_.append(holy_friday)

    # Corpus Christi
    corpus_christi = easter_ + dt.timedelta(days=60)
    holidays_.append(corpus_christi)

    return holidays_


def increment_month(year, month, increment=1):
    '''Increments month by increment and returns the resulting year and month'''
    if not all((isinstance(x, int) for x in (year, month, increment))):
        raise TypeError('year, month and increment must be integers')
    if not 1 <= month <= 12:
        raise ValueError('invalid month {}'.format(month))
    month += increment
    while 12 < month:
        month -= 12
        year += 1
    return year, month


def first_workday(date):
    '''Evaluates the first workday since date'''
    holidays_ = holidays(date.year)
    while date in holidays_ or date.weekday() in (5, 6):
        date = date + dt.timedelta(days=1)
    return date


class B3FutureContract:
    '''Future contract from B3 exchange base class'''
    _names = ()
    _series = 'FGHJKMNQUVXZ'

    def __init__(self, date=None):
        if date is not None and not isinstance(date, dt.date):
            raise TypeError('date must be a datetime.date object')
        self.date = date if date is not None else dt.date.today()

    def serie_of_month(self, month):
        '''Returns the serie of the contract at month'''
        raise NotImplementedError()

    def rollover_date(self, date):
        '''Evaluates the rollover date of the contract'''
        raise NotImplementedError()

    @staticmethod
    def __format_name(name, serie, rolldate):
        '''Format the contract name'''
        return '{}{}{}'.format(name, serie, rolldate.strftime('%y'))

    def current_name(self, date=None):
        '''Returns the names of the current contract on date'''
        if date is None:
            date = self.date
        rolldate = self.rollover_date(date)
        serie = self.serie_of_month(rolldate.month)
        names = (
            self.__format_name(self._names[0], serie, rolldate),
            self.__format_name(self._names[1], serie, rolldate)
        )
        return names


class B3FutureIndex(B3FutureContract):
    '''Future index contract rollover date class'''
    _names = ('WIN', 'IND')

    def serie_of_month(self, month):
        if not isinstance(month, int):
            raise TypeError('month must be an integer')
        if not 1 <= month <= 12:
            raise ValueError('invalid month {}'.format(month))
        if month % 2 != 0:
            raise ValueError('odd month {}'.format(month))
        return self._series[month - 1]

    def rollover_date(self, date=None):
        '''The rollover date of the future index contract is the
        nearest wednesday to the 15th day of the even months, or the
        first subsequent workday'''
        if date is None:
            date = self.date
        elif not isinstance(date, dt.date):
            raise TypeError('date must be a datetime.date object')
        year, month = date.year, date.month
        if month % 2 != 0:
            year, month = increment_month(year, month)
        basedate = dt.date(year, month, 15)
        offset0 = 2 - basedate.weekday()
        offset1 = 7 + offset0
        offset = offset0 if abs(offset0) < abs(offset1) else offset1
        rolldate = basedate + dt.timedelta(days=offset)
        rolldate = first_workday(rolldate)
        if rolldate <= date:
            year, month = increment_month(year, month, 2)
            rolldate = self.rollover_date(dt.date(year, month, 1))
        return rolldate


class B3FutureDollar(B3FutureContract):
    '''Future dollar contract rollover date class'''
    _names = ('WDO', 'DOL')

    def serie_of_month(self, month):
        if not isinstance(month, int):
            raise TypeError('month must be an integer')
        if not 1 <= month <= 12:
            raise ValueError('invalid month {}'.format(month))
        return self._series[month - 1]

    def rollover_date(self, date=None):
        '''The rollover date of the future dollar contract is the
        first workday of each month'''
        if date is None:
            date = self.date
        elif not isinstance(date, dt.date):
            raise TypeError('date must be a datetime.date object')
        year, month = date.year, date.month
        year, month = increment_month(year, month)
        basedate = dt.date(year, month, 1)
        rolldate = first_workday(basedate)
        return rolldate


def main(year):
    '''Tests the classes with some arbitrary dates'''
    index = B3FutureIndex()
    dollar = B3FutureDollar()
    for month in range(1, 13):
        for day in (5, 20):
            date = dt.date(year, month, day)
            print(date, end='  ')

            rolldate = index.rollover_date(date)
            contract = index.current_name(date)[0]
            print(rolldate, contract, end='  ')

            rolldate = dollar.rollover_date(date)
            contract = dollar.current_name(date)[0]
            print(rolldate, contract)


if __name__ == '__main__':
    import sys
    if 1 < len(sys.argv):
        YEAR = int(sys.argv[1])
    else:
        YEAR = dt.date.today().year
    main(YEAR)
