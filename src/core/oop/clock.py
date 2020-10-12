import os
import time


class Clock(object):
    def __init__(self, **kwargs):
        if 'hour' in kwargs and 'minute' in kwargs and 'second' in kwargs:
            self._hour = kwargs['hour']
            self._minute = kwargs['minute']
            self._second = kwargs['second']
        else:
            tm = time.localtime(time.time())
            self._hour = tm.tm_hour
            self._minute = tm.tm_min
            self._second = tm.tm_sec

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '{:02d}:{:02d}:{:02d}' \
            .format(self._hour, self._minute, self._second)


def main():
    clock = Clock()
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print(clock.show())
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
