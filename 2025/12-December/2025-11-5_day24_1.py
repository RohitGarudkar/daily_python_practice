#Python Datetime Module
import datetime
import pytz
dt1 = datetime.datetime.now(pytz.timezone('asia/kolkata'))
print(dt1)
dt2 = datetime.datetime.now(pytz.timezone('asia/karachi'))
print(dt2)
dt3 = datetime.datetime.now(pytz.timezone('asia/colombo'))
print(dt3)

