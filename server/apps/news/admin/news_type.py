from django.contrib import admin

from ..models import NewsType


@admin.register(NewsType)
class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name', 'color')
