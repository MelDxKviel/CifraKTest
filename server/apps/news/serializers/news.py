from rest_framework import serializers

from ..models import News, NewsType
from .news_type import NewsTypeSerializer


class NewsRetrieveSerializer(serializers.ModelSerializer):
    type = NewsTypeSerializer()

    class Meta:
        model = News
        fields = '__all__'


class NewsListSerializer(serializers.ModelSerializer):
    type = NewsTypeSerializer()

    class Meta:
        model = News
        fields = ('title', 'short_description', 'type')


class NewsCreateSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset=NewsType.objects.all())

    class Meta:
        model = News
        fields = '__all__'
