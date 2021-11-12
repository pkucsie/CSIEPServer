import datetime
import time

from app_api.models import SysLog


def get_order_no():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    if month < 10:
        month = f'0{month}'
    if day < 10:
        day = f'0{day}'
    return f'{year}{month}{day}{int(time.time())}'


def log_save(user, request, flag, message, log_type):
    log = SysLog(
        user_name=user,
        ip_addr=request.META['REMOTE_ADDR'],
        action_flag=flag,
        message=message,
        log_type=log_type
    )
    log.save()

'''
convert timeval
xx前的时间格式
'''
def get_agostr(timeval):
    n = timeval/1000
    # d = datetime.timedelta(seconds=timeval)
    # dt = datetime.datetime.now() - d
    # print(dt)
    # print(time.localtime(n))
    datetime_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(n))
    dt = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    dtnow = datetime.datetime.now()
    delta = dtnow - dt

    years = delta.days//365
    months = delta.days//30
    days = delta.days
    hours = int(delta.seconds / 3600)
    minutes = int(delta.seconds % 3600 / 60)
    seconds = delta.seconds % 3600 % 60
    # print(help(delta))
    if years > 0: return str(years)+'年前'
    if months > 0: return str(months) + '月前'
    if days > 0: return str(days) + '天前'
    if hours > 0: return str(years) + '小时前'
    if minutes > 0: return str(minutes) + '分钟前'
    if seconds >= 30: return str(seconds) + '秒前'
    if seconds < 30: return '刚刚'

    return ''


def get_ymd(timeval):
    n = timeval/1000
    dt_str = time.strftime('%Y-%m-%d', time.localtime(n))
    return str(dt_str)


def get_age(timeval):
    n = timeval/1000
    dt_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(n))
    dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dtnow = datetime.datetime.now()
    delta = dtnow - dt

    years = delta.days//365

    return str(years)+'岁'

# 今天 12:36
# 34分钟前
# 20秒前
# 2月26日 09:38
# 统一格式化成时间类型
def get_format_datetime(datestr):
    now = datetime.datetime.now()
    ymd = now.strftime("%Y-%m-%d")
    y = now.strftime("%Y")
    newdate = now
    if (u"今天" in datestr):
        mdate = time.mktime(time.strptime(ymd + datestr, '%Y-%m-%d今天 %H:%M'))
        newdate = datetime.datetime.fromtimestamp(mdate)
    elif (u"月" in datestr):
        mdate = time.mktime(time.strptime(y + datestr, '%Y%m月%d日 %H:%M'))
        newdate = datetime.datetime.fromtimestamp(mdate)
    elif (u"分钟前" in datestr):
        # print(datestr[:-3])
        newdate = now - datetime.timedelta(minutes=int(datestr[:-3]))
    elif (u"秒前" in datestr):
        newdate = now - datetime.timedelta(minutes=int(datestr[:-2]))
    else:
        newdate = datetime.datetime.strptime(datestr, "%Y-%m-%d %H:%M")
    return newdate

# #print(get_format_datetime("3分钟前"))
# print(get_timestring(638208000))
# print(get_timestring(1536525302))
# print(get_timestring(1636525302))
# print(getAge(638208000))

