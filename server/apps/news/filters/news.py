from django_filters import rest_framework as filters

from ..models import News


class NewsFilter(filters.FilterSet):
    class Meta:
        model = News
        fields = ['type', ]
