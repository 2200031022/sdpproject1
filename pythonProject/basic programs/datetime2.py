import calendar
s=calendar.prcal(3023)
s2=calendar.month(2023,4)
s1=calendar.isleap(2005)
print(s1)




import datetime
x=datetime.datetime.now()
from datetime import timedelta
print(x+timedelta(days=-89))



import time
from datetime import datetime
import pytz
time1=pytz.timezone('Indian/Maldives')
print("Current Time is:",datetime.now(time1))
