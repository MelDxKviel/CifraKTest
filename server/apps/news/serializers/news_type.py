from rest_framework import serializers

from ..models import NewsType


class NewsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsType
        fields = '__all__'
