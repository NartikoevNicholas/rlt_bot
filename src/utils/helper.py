import datetime

from typing import Literal


Step = Literal['hour', 'day', 'week', 'month']


def next_date(date: datetime.datetime, step: Step):
    date = date.replace(minute=0, second=0, microsecond=0)
    if step == 'hour':
        date += datetime.timedelta(hours=1)
    elif step == 'day':
        date += datetime.timedelta(days=1)
        date = date.replace(hour=0)
    elif step == 'week':
        count = 7 - date.weekday()
        date += datetime.timedelta(days=count)
        date = date.replace(hour=0)
    elif step == 'month':
        if date.month < 12:
            date = date.replace(month=date.month + 1, day=1)
        else:
            date = date.replace(year=date.year + 1, month=1, day=1)
    return date
