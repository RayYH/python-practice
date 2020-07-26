from datetime import datetime
import pytz


def main():
    tz_new_york = pytz.timezone('America/New_York')
    datetime_new_york = datetime.now(tz_new_york)
    tz_london = pytz.timezone('Europe/London')
    datetime_london = datetime.now(tz_london)
    print("New York:", datetime_new_york)
    print("London:", datetime_london)


if __name__ == '__main__':
    main()
