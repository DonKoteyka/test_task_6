from django_filters import DateFromToRangeFilter
from django_filters import rest_framework as filters

from application.models import Posts

# class AdvertisementFilter(filters.FilterSet):
#
#     """Фильтры для объявлений."""
#     created_at = DateFromToRangeFilter()
#
#
#
#     class Meta:
#         model = Posts
#         fields = ['creator', 'status']
