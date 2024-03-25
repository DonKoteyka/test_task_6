from django_filters import rest_framework as filters, DateFromToRangeFilter

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
