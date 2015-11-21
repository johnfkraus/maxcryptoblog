# File: datetime-example_2.py
import datetime
#  import datetime, date, time, timedelta
import time
import inspect


def lineno():
    """ Returns the current line number in the program.
    Danny Yoo (dyoo@hkn.eecs.berkeley.edu).
    Requires import inspect.
    """
    return inspect.currentframe().f_back.f_lineno


class EmailMessage():
    created_date = datetime.datetime.now()

    def __str__(self):
        return ('date = ' + str(self.created_date))


e = EmailMessage()
print('e = ', e)

mytdelta = datetime.timedelta(-1, 0, 0)  # Interval of -1 day and 0.0 seconds


def created_in_last_day(e):
    mytdelta = datetime.timedelta(-1, 0, 0)  # Interval of -1 day and 0.0 seconds
    not_since_time = datetime.datetime.now() + mytdelta
    print(lineno(), 'not_since_time=', not_since_time)
    if e.created_date > not_since_time:
        return 1
    else:
        return 0


print(lineno(), created_in_last_day(e))





def print_datetime(now):
    print(now)
    print(repr(now))
    print(type(now))
    print(now.year, now.month, now.day)
    print(now.hour, now.minute, now.second)
    print(now.microsecond)
    print()

t1 = datetime.datetime(2003, 8, 4, 12, 30, 45)

print(lineno(), 'datetime.datetime(2003, 8, 4, 12, 30, 45) =', t1)
print_datetime(t1)

t2 = datetime.datetime.now()
time.sleep(2)  # delays for 5 seconds
t3 = datetime.datetime.now()
print(lineno(), 'datetime.now() =', t2)
print_datetime(t2)


mytdelta = datetime.timedelta(1, 0, 0)  # Interval of 1 day and 5.41038 seconds
secs = mytdelta.total_seconds()
hours = (secs / 3600)
minutes = (secs / 60)

print(lineno(), 'secs=', secs, 'hours=', hours, 'minutes=', minutes)
"""
mytdelta = datetime.timedelta(1, 5, 41038)  # Interval of 1 day and 5.41038 seconds
secs = mytdelta.total_seconds()
hours = (secs / 3600)
minutes = (secs / 60)

hours = int(secs / 3600)
minutes = int(secs / 60) % 60
"""

# print('secs=', secs, 'hours=', hours, 'minutes=', minutes)
dur = t2 - t1
print('dur.__class__ = ', dur.__class__)

dur2 = t3 - t2

secs = dur2.total_seconds()
hours = (secs / 3600)
minutes = (secs / 60)
print('secs=', secs, 'hours=', hours, 'minutes=', minutes)



