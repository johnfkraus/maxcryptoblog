from datetime import datetime, date, time
# Using datetime.combine()
d = date(2005, 7, 14)
t = time(12, 30)
datetime.combine(d, t)
datetime.datetime(2005, 7, 14, 12, 30)
# Using datetime.now() or datetime.utcnow()
datetime.now()   
datetime.datetime(2007, 12, 6, 16, 29, 43, 79043)   # GMT +1
datetime.utcnow()   
datetime.datetime(2007, 12, 6, 15, 29, 43, 79060)
# Using datetime.strptime()
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
 dt
datetime.datetime(2006, 11, 21, 16, 30)
 # Using datetime.timetuple() to get tuple of all attributes
 tt = dt.timetuple()
 for it in tt:   
...     print it
...
2006    # year
11      # month
21      # day
16      # hour
30      # minute
0       # second
1       # weekday (0 = Monday)
325     # number of days since 1st January
-1      # dst - method tzinfo.dst() returned None
 # Date in ISO format
 ic = dt.isocalendar()
 for it in ic:   
...     print it
...
2006    # ISO year
47      # ISO week
2       # ISO weekday
 # Formatting datetime
 dt.strftime("%A, %d. %B %Y %I:%M%p")
'Tuesday, 21. November 2006 04:30PM'
 'The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(dt, "day", "month", "time")
'The day is 21, the month is November, the time is 04:30PM.'

Using datetime with tzinfo:


 from datetime import timedelta, datetime, tzinfo
 class GMT1(tzinfo):
...     def utcoffset(self, dt):
...         return timedelta(hours=1) + self.dst(dt)
...     def dst(self, dt):
...         # DST starts last Sunday in March
...         d = datetime(dt.year, 4, 1)   # ends last Sunday in October
...         self.dston = d - timedelta(days=d.weekday() + 1)
...         d = datetime(dt.year, 11, 1)
...         self.dstoff = d - timedelta(days=d.weekday() + 1)
...         if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
...             return timedelta(hours=1)
...         else:
...             return timedelta(0)
...     def tzname(self,dt):
...          return "GMT +1"
...
 class GMT2(tzinfo):
...     def utcoffset(self, dt):
...         return timedelta(hours=2) + self.dst(dt)
...     def dst(self, dt):
...         d = datetime(dt.year, 4, 1)
...         self.dston = d - timedelta(days=d.weekday() + 1)
...         d = datetime(dt.year, 11, 1)
...         self.dstoff = d - timedelta(days=d.weekday() + 1)
...         if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
...             return timedelta(hours=1)
...         else:
...             return timedelta(0)
...     def tzname(self,dt):
...         return "GMT +2"
...
 gmt1 = GMT1()
 # Daylight Saving Time
 dt1 = datetime(2006, 11, 21, 16, 30, tzinfo=gmt1)
 dt1.dst()
datetime.timedelta(0)
 dt1.utcoffset()
datetime.timedelta(0, 3600)
 dt2 = datetime(2006, 6, 14, 13, 0, tzinfo=gmt1)
 dt2.dst()
datetime.timedelta(0, 3600)
 dt2.utcoffset()
datetime.timedelta(0, 7200)
 # Convert datetime to another time zone
 dt3 = dt2.astimezone(GMT2())
 dt3     
datetime.datetime(2006, 6, 14, 14, 0, tzinfo=<GMT2 object at 0x...>)
 dt2     
datetime.datetime(2006, 6, 14, 13, 0, tzinfo=<GMT1 object at 0x...>)
 dt2.utctimetuple() == dt3.utctimetuple()
True

8.1.5. time Objects

A time object represents a (local) time of day, independent of any particular day, and subject to adjustment via a tzinfo object.

class datetime.time([hour[, minute[, second[, microsecond[, tzinfo]]]]])

    All arguments are optional. tzinfo may be None, or an instance of a tzinfo subclass. The remaining arguments may be ints or longs, in the following ranges:

        0 <= hour < 24
        0 <= minute < 60
        0 <= second < 60
        0 <= microsecond < 1000000.

    If an argument outside those ranges is given, ValueError is raised. All default to 0 except tzinfo, which defaults to None.

Class attributes:

time.min

    The earliest representable time, time(0, 0, 0, 0).

time.max

    The latest representable time, time(23, 59, 59, 999999).

time.resolution