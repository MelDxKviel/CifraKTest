from rest_framework.routers import DefaultRouter

from .viewsets import NewsTypeViewSet, NewsViewSet


news_router = DefaultRouter()

news_router.register(
    prefix='news',
    viewset=NewsViewSet,
    basename='news',
)

news_router.register(
    prefix='types',
    viewset=NewsTypeViewSet,
    basename='types',
)
