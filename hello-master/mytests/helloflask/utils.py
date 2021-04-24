from datetime import date, datetime, timedelta

def make_date(dt, fmt):
    if not isinstance(dt, date):
        return datetime.strptime(dt, fmt)
    else:
        return dt
