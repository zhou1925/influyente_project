from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Stat
from .utils import get_views_by_date


@api_view(['GET'])
def getStats(request, pk):
    """ get views history of  profile """
    stat_obj = Stat.objects.get(pk=pk)

    total = stat_obj.views

    month = get_views_by_date(stat_obj, total, days=30)
    week = get_views_by_date(stat_obj, total, days=7)
    day = get_views_by_date(stat_obj, total, days=1)
    data = {
        'total_views': total,
        'month': month,
        'week': week,
        'day': day
    }
    return Response(data)
