##时间
#datetime是Python处理日期和时间的标准库。
#当然还有time


from datetime import datetime

#取当前日期和时间
now = datetime.now()
print(now)
print(type(now))

#获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)


#datetime转换为timestamp
#时间戳
#timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00 是以1970为0点

dt = datetime(2015, 4, 19, 12, 20)
tam = dt.timestamp()
print(tam)

###市区设置
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间
# 2015-04-19 12:20:00
# 2015-04-19 04:20:00


#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday) #2015-06-01 18:19:59


#datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M')) #Thu, Feb 08 11:40



#datetime加减

from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=1,hours=12))


#本地时间转换为UTC时间
#设置时区 replace     timezone时区是哪个
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)


#时区转换 先通过utcnow()拿到当前的UTC时间，astimezone再转换为任意时区的时间：
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))


time_8 = timezone(timedelta(hours=8))





# 练习
#
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
# 以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
#
import re
def to_timestamp(dt_str, tz_str):
    s_date = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    #print(re.match('UTC((\+|-)\d+):00',tz_str))
    mart = re.match('UTC((\+|-)\d+):00',tz_str)
    if mart:
        t = mart.group(1)
    else:
        t = 0
    t2= int(t)
    # t2 = 8-int(t)
    # new_date = s_date + timedelta(hours=t2)
    # return new_date.timestamp()
    tz_utc_in = timezone(timedelta(hours=t2))
    dt = s_date.replace(tzinfo=tz_utc_in)
    return dt.timestamp()





t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
#print('===='+str(t1))
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
#print(t2)
assert t2 == 1433121030.0, t2

print('ok')






























