from django_filters import rest_framework as filters
from .models import Profile

class ProfilesFilter(filters.FilterSet):

    location = filters.CharFilter(field_name='location', lookup_expr='icontains')
    max_age = filters.NumberFilter(field_name="age" or 100, lookup_expr='lte')
    min_age = filters.NumberFilter(field_name="age" or 0, lookup_expr='gte')
    class Meta:
        model = Profile
        fields = ('location', 'max_age', 'min_age')
