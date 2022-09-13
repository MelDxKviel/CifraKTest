from django.urls import path, include

from apps.news.routers import news_router
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('', include(news_router.urls)),
    path('schema/', get_schema_view())
]
