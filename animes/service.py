from django_filters import rest_framework as filters
from .models import Anime


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class AnimeFilter(filters.FilterSet):
    genres = CharFilterInFilter(field_name='genres__name', lookup_expr='in')
    year = filters.RangeFilter()
    status = CharFilterInFilter(field_name='status__name', lookup_expr='in')
    type = CharFilterInFilter(field_name='type__name', lookup_expr='in')
    producer = CharFilterInFilter(field_name='type__name', lookup_expr='in')

    class Meta:
        model = Anime
        fields = ['genres', 'year', 'status', 'type', 'producer']
