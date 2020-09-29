from datetime import datetime
import pytz


def test_timezone():
    tz_new_york = pytz.timezone('America/New_York')
    datetime_new_york = datetime.now(tz_new_york)
    tz_london = pytz.timezone('Europe/London')
    datetime_london = datetime.now(tz_london)
    assert datetime_new_york.strftime("%H") != datetime_london.strftime("%H")
