from rest_framework import viewsets
from ..models import NewsType

from ..serializers import NewsTypeSerializer
from ..models.querysets import NewsTypeQuerySet


class NewsTypeViewSet(viewsets.ModelViewSet):
    serializer_class = NewsTypeSerializer

    def get_queryset(self) -> NewsTypeQuerySet:
        return NewsType.objects.order_by(
            '-id',
            'name',
        )

