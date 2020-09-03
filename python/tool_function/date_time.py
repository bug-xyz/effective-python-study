"""
日期和时间相关操作
"""
import datetime
import time


def choice_date(day, str_date=None):
    """
    功能说明      基于某个时间的时间函数，day为正数表示day天后；为负数表示day天前
    --------------------------------
    修改人        修改时间        修改原因
    --------------------------------
    方朋        2014-03-24
    说明：如果str_date=None，则基于当前时间；否则是基于str_date这个时间
    """
    now = datetime.datetime.now()
    hope_date_format = now + datetime.timedelta(days=day)
    hope_date = hope_date_format.strftime('%Y-%m-%d %H:%M:%S')
    if str_date:
        tem = time.mktime(time.strptime(str_date, '%Y-%m-%d %H:%M:%S'))
        x = time.localtime(tem)
        date = datetime.datetime(x.tm_year, x.tm_mon, x.tm_mday, x.tm_hour, x.tm_min, x.tm_sec)
        hope_date = date + datetime.timedelta(days=day)
    print(hope_date)
    return ''


if __name__ == '__main__':
    pass
    # choice_date(1, '2020-7-6 11:21:30')

