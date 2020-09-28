from datetime import date, time, datetime, timedelta

# http://pytz.sourceforge.net/


def test_date():
    a_date = date(2020, 7, 26)
    assert '{}'.format(a_date) == '2020-07-26'
    timestamp = date.fromtimestamp(1326244364)
    assert '{}'.format(timestamp) == '2012-01-11'
    today = date.today()
    assert today.year
    assert today.month
    assert today.day
    a_time = time(11, 34, 56)
    assert '{}'.format(time()) == '00:00:00'
    assert '{}'.format(a_time) == '11:34:56'
    c = time(hour=11, minute=34, second=56)
    assert '{}'.format(c) == '11:34:56'
    d = time(11, 34, 56, 234566)
    assert '{}'.format(d) == '11:34:56.234566'
    assert d.hour
    assert d.minute
    assert d.second
    assert d.microsecond
    a_datetime = datetime(2017, 11, 28, 23, 55, 59, 342380)
    assert '{}'.format(a_datetime) == '2017-11-28 23:55:59.342380'
    assert a_datetime.year == 2017
    assert a_datetime.month == 11
    assert a_datetime.day == 28
    assert a_datetime.hour == 23
    assert a_datetime.minute == 55
    assert a_datetime.second == 59
    assert a_datetime.microsecond == 342380
    assert a_datetime.timestamp()  # influenced by timezone


def test_difference_between_two_datetime():
    t1 = date(year=2018, month=7, day=12)
    t2 = date(year=2017, month=12, day=23)
    t3 = t1 - t2
    assert '{}'.format(t3) == '201 days, 0:00:00'
    t4 = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
    t5 = datetime(year=2019, month=6, day=10, hour=5, minute=55, second=13)
    t6 = t4 - t5
    assert '{}'.format(t6) == '-333 days, 1:14:20'
    assert '{}'.format(type(t3)) == "<class 'datetime.timedelta'>"
    assert '{}'.format(type(t6)) == "<class 'datetime.timedelta'>"
    t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
    t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
    t3 = t1 - t2
    assert '{}'.format(t3) == '14 days, 13:55:39'
    t1 = timedelta(seconds=33)
    t2 = timedelta(seconds=54)
    t3 = t1 - t2
    assert '{}'.format(t3) == '-1 day, 23:59:39'
    assert '{}'.format(abs(t3)) == '0:00:21'


def test_duration_seconds():
    t = timedelta(days=5, hours=1, seconds=33, microseconds=233423)
    assert t.total_seconds() == 435633.233423


def test_date_format():
    t = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
    assert t.strftime("%H:%M:%S") == "07:09:33"
    assert t.strftime("%m/%d/%Y, %H:%M:%S") == "07/12/2018, 07:09:33"


def test_strptime():
    date_string = "21 June, 2018"
    date_object = datetime.strptime(date_string, "%d %B, %Y")
    assert '{}'.format(date_object) == '2018-06-21 00:00:00'
