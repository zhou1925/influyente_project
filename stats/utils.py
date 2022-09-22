from .models import Stat
from django.utils import timezone
from datetime import timedelta


def getPercentage(part, total):
    return 100 * float(part) / float(total)

def get_views_by_date(stat, total_views, days):
    """ calculate views gained by specifying a date range """
    date = timezone.now() - timedelta(minutes=days)
    last_views = stat.history.filter(updated__lte=date)
    if len(last_views) > 0:
        last_view_val = last_views.first().views
        diff = total_views - last_view_val
        return getPercentage(last_view_val, total_views)
    return None
