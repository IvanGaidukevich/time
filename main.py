class Time:
    """
    For keeping time in seconds
    """

    def __init__(self, hh: int, mm: int, ss: int):
        self.hour = hh
        self.minute = mm
        self.second = ss

    def convert(self):
        """
        Returns time converted into seconds from fields of Time object. All negative numbers will be converted
        to positive numbers.
        """
        return abs(self.hour) * 3600 + abs(self.minute) * 60 + abs(self.second)

    def __str__(self):
        """
        Returns string with time in seconds
        """
        return f'{self.convert()}'

    def __eq__(self, other):
        """
        Returns True if the time value of self is equal to the time value of other
        """
        return self.convert() == other.convert()

    def __lt__(self, other):
        """
        Returns True if the time value of self is less than time value of other
        """
        return self.convert() < other.convert()

    def __gt__(self, other):
        """
        Returns True if the time value of self is greater than time value of other
        """
        return self.convert() > other.convert()

    def __hash__(self):
        return hash((self.hour, self.minute, self.second))

    def __repr__(self):
        return str(self) + f'; hash: {hash(self)}'

    def __add__(self, other):
        """
        Sum of time values in seconds of two objects Time
        """
        return self.convert() + other.convert()

    def __sub__(self, other):
        """
        Difference between time values of two Time objects.
        Method always returns time in seconds greater than or equal to zero
        """
        if self.convert() - other.convert() > 0:
            return self.convert() - other.convert()
        else:
            return 0


class TimeAlt:
    """
    For keeping time in format dd:hh:mm:ss
    """

    def __init__(self, hh: int, mm: int, ss: int, dd=0):
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.day = dd

    def convert(self):
        sec = self.day * 86400 + self.hour * 3600 + self.minute * 60 + self.second
        self.day = sec // 86400
        self.hour = sec % 86400 // 3600
        self.minute = sec % 86400 % 3600 // 60
        self.second = sec % 86400 % 60
        return sec

    def __str__(self):
        self.convert()
        return f'{self.day:02d}:{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __eq__(self, other):
        return self.convert() == other.convert()

    def __hash__(self):
        return hash((self.second, self.minute, self.hour, self.day))

    def __repr__(self):
        return str(self) + f'; hash: {hash(self)}'

    def __add__(self, other):
        self.day += other.day
        self.hour += other.hour
        self.minute += other.minute
        self.second += other.second
        return self

    def __sub__(self, other):
        """
        Difference between time values of two Time objects.
        Method always returns time in seconds greater than or equal to zero
        """
        if self.convert() - other.convert() > 0:
            self.day -= other.day
            self.hour -= other.hour
            self.minute -= other.minute
            self.second -= other.second
        else:
            self.day = 0
            self.hour = 0
            self.minute = 0
            self.second = 0
        return self


class NanoTime(Time):
    """
    For keeping time in nanoseconds
    """

    def __init__(self, hh: int, mm: int, ss: int, ms: int, mcs: int, ns: int):
        super().__init__(hh, mm, ss)
        self.milli_sec = ms
        self.micro_sec = mcs
        self.nano_sec = ns

    def convert(self):
        """
        Returns time converted into nanoseconds from fields of NanoTime object.
        All negative numbers will be converted to positive numbers.
        """
        return abs(self.hour) * 3600000000000 + abs(self.minute) * 60000000000 + abs(self.second) * 1000000000 + \
            abs(self.milli_sec) * 1000000 + abs(self.micro_sec) * 1000 + abs(self.nano_sec)

    def __str__(self):
        return f'{self.convert()}'

    def __eq__(self, other):
        return self.convert() == other.convert()

    def __lt__(self, other):
        """
        Returns True if the time value of self is less than time value of other
        """
        return self.convert() < other.convert()

    def __gt__(self, other):
        """
        Returns True if the time value of self is greater than time value of other
        """
        return self.convert() > other.convert()

    def __hash__(self):
        return hash((self.hour, self.minute, self.second, self.milli_sec, self.micro_sec, self.nano_sec))

    def __repr__(self):
        return str(self) + f'; hash: {hash(self)}'

    def __add__(self, other):
        return self.convert() + other.convert()

    def __sub__(self, other):

        """
        Difference between time values of two Time objects.
        Method always returns time in nanoseconds greater than or equal to zero.
        """

        if self.convert() - other.convert() > 0:
            return self.convert() - other.convert()
        else:
            return 0


class TimeNanoTimeComparator:
    """
    For comparing Time with NanoTime
    """

    @staticmethod
    def comparator(time: Time, nanotime: NanoTime):
        """
        Method returns True if Time > NanoTime, False if Time<NanoTime, None if Time == NanoTime
        """
        t = time.convert() * 1000000000
        nt = nanotime.convert()
        if t > nt:
            return True
        elif t < nt:
            return False
        else:
            return None


time_stamp1 = Time(0, 1, 0)
time_stamp2 = Time(1, 1, 1)
print(f'{time_stamp1!r}')
print(f'{time_stamp2!r}')
print(time_stamp1 == time_stamp2)
print(time_stamp1 < time_stamp2)

time_stamp3 = TimeAlt(72, 61, 0)
time_stamp4 = TimeAlt(24, 1, 1)
print(f'{time_stamp3!r}')
print(f'{time_stamp4!r}')
print(time_stamp3 == time_stamp4)

time_stamp5 = NanoTime(1, 1, 1, 1, 1, 1)
time_stamp6 = NanoTime(1, 1, 1, 0, 0, 0)
print(f'{time_stamp5!r}')
print(f'{time_stamp6!r}')
print(time_stamp5 == time_stamp6)
print(time_stamp6 > time_stamp5)

print(TimeNanoTimeComparator.comparator(time_stamp2, time_stamp6))  # they are equal
