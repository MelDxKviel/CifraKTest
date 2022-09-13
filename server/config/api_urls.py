from django.urls import path, include

from apps.news.routers import news_router


urlpatterns = [
    path('', include(news_router.urls))
]
