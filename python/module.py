# 3types:

# 1. built-in (datetime,math)
# 2. Custom (user defined)
# 3. External (pandas,numpy)


# 1. built-in
# 1.datetime

import datetime 
print(datetime.datetime.now())

import datetime as dt
print(dt.datetime.now())

cur_date=dt.datetime.now()
print(cur_date.year)
print(cur_date.strftime("%S"))

import math 
a=10.6
b=10.4
print(math.ceil(a))
print(math.ceil(b))
print(math.floor(a))
print(math.floor(b))
print(round(a))
print(round(b))

import calculation as c 
print(c.addition(12,23))
c.subtraction(23,45)

