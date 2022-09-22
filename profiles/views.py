import redis
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from cacheops import cached_view_as
from rest_framework import status
from django.db.models import Count
from ratelimit.decorators import ratelimit
from .models import Profile
from .serializers import ProfileSerializer, MinProfileSerializer
from .filters import ProfilesFilter


# set DB 1 for Leadboard
r = redis.Redis(host='localhost',port=6379, db=1)


#@cached_view_as(Profile, timeout=60*60*24)
@api_view(['GET'])
def getNewProfls(request):
    """ return new_profiles based on -created and photos > 1"""
    profls = Profile.objects.annotate(photos_count=Count('user__photos')).filter(photos_count__gte=1,active=True).order_by('-created')[:3]
    
    serializer = MinProfileSerializer(profls, many=True)
    
    return Response({"profiles": serializer.data})

#@cached_view_as(Profile, timeout=60*60*4)
@api_view(['GET'])
def leadboard(request):
    """ 
    return the first 3 profiles ranked by redis
    four hours cached
    """
    profls = r.zrevrange("profiles", 0, 2) # get first 3 ids in reverse order
    profls_ids = [int(p_id) for p_id in profls]
    qs = Profile.objects.annotate(photos_count=Count('user__photos'))
    qs = list(qs.filter(photos_count__gte=1, id__in=profls_ids, active=True).order_by('?'))
    count = len(qs)

    serializer = MinProfileSerializer(qs, many=True)

    return Response({'profiles': serializer.data, 'count':count})

@cached_view_as(Profile, timeout=60)
@api_view(['GET'])
def feed(request):
    profiles = Profile.objects.order_by('-isBoost', 'last_boost_type', '?')    
    filterset = ProfilesFilter(request.GET, queryset=profiles)

    resPerPage = 20
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage
    
    queryset = paginator.paginate_queryset(filterset.qs, request)
    count = filterset.qs.count()

    serializer = ProfileSerializer(queryset, many=True)

    return Response({
        "count": count,
        "resPerPage": resPerPage, 
        "profiles": serializer.data
    })

@ratelimit(key='ip', rate='20/m', block=True)
@api_view(['GET'])
def getProfile(request, username):
    """ get profile by username
    if one ip is trying to send a lot api calls will be blocked
    """
    profile = get_object_or_404(Profile, user__username=username, active=True)
    # redis 
    incr_value = 1

    if profile:
        profile_id = profile.id

        r.zincrby("profiles", incr_value, profile_id)

        serializer = ProfileSerializer(profile, many=False)
        return Response({'profile': serializer.data})

