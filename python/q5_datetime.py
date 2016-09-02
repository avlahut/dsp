# Hint:  use Google to find python function
from datetime import date
import calendar
####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'
(monthStart, dayStart, yearStart) = date_start.split('-')
(monthStop, dayStop, yearStop) = date_stop.split('-')

d0 = date(int(yearStart),int(monthStart),int(dayStart))
d1 = date(int(yearStop),int(monthStop),int(dayStop))
deltaA = d1 - d0
print(deltaA.days)

####b)
date_start = '12312013'
date_stop = '05282015'

d0 = date(int(date_start[4:]),int(date_start[:2]),int(date_start[2:4]))
d1 = date(int(date_stop[4:]),int(date_stop[:2]),int(date_stop[2:4]))
deltaB = d1 - d0
print(deltaB.days)

####c)

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
(dayStart, monthStart, yearStart) = date_start.split('-')
(dayStop,monthStop,  yearStop) = date_stop.split('-')

monthStartInt = list(calendar.month_abbr).index(monthStart)
monthStopInt = list(calendar.month_abbr).index(monthStop)

d0 = date(int(yearStart),monthStartInt,int(dayStart))
d1 = date(int(yearStop),monthStopInt,int(dayStop))
deltaC = d1 - d0
print(deltaC.days)
