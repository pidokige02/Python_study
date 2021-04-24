from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

from helloflask import app
from helloflask.utils import make_date


@app.template_filter('artist_names')
def artist_names(artists):
    # ['<a href="/artists/%s">%s</a>' % (a.artist.artistid, a.artist.name)]
    return ", ".join([a.artist.name for a in artists])


@app.template_filter('ymd')               # cf. Handlebars' helper
def datetime_ymd(dt, fmt='%m-%d'):
    if isinstance(dt, date):
        return "<strong>%s</strong>" % dt.strftime(fmt)
    else:
        return dt


@app.template_filter('simpledate')
def simpledate(dt):
    if not isinstance(dt, date):
        dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')

    # if ( datetime.now() - dt) < timedelta(1):
    if (datetime.now() - dt).days < 1:
        fmt = "%H:%M"
    else:
        fmt = "%m/%d"

    return "<strong>%s</strong>" % dt.strftime(fmt)


@app.template_filter('sdt')
def sdt(dt, fmt='%Y-%m-%d'):
    d = make_date(dt, fmt)
    wd = d.weekday()
    # if wd == 6:
    #     return 1
    # else:
    #     return wd
    return (1 if wd == 6 else wd) * -1


@app.template_filter('month')
def month(dt, fmt='%Y-%m-%d'):
    d = make_date(dt, fmt)
    return d.month


@app.template_filter('edt')
def edt(dt, fmt='%Y-%m-%d'):
    d = make_date(dt, fmt)
    nextMonth = d + relativedelta(months=1)
    return (nextMonth - timedelta(1)).day + 1
