from typing import Type

from rest_framework import viewsets
from ..models import News
from ..models.querysets import NewsQuerySet

from ..serializers import (
    NewsRetrieveSerializer,
    NewsCreateSerializer,
    NewsListSerializer,
)


class NewsViewSet(viewsets.ModelViewSet):
    filterset_fields = ('type',)

    def get_serializer_class(self) -> Type[NewsListSerializer | NewsCreateSerializer | NewsRetrieveSerializer]:
        if self.action == 'create':
            serializer_class = NewsCreateSerializer
        elif self.action == 'list':
            serializer_class = NewsListSerializer
        else:
            serializer_class = NewsRetrieveSerializer

        return serializer_class

    def get_queryset(self) -> NewsQuerySet:
        return News.objects.order_by(
            '-id',
            'title',
        )
