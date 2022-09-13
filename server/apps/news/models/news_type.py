from django.db import models

from .managers import NewsTypeManager


class NewsType(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название типа новости'
    )
    color = models.CharField(
        max_length=31,
        verbose_name='Цвет'
    )

    objects = NewsTypeManager()

    class Meta:
        verbose_name = 'Тип новости'
        verbose_name_plural = 'Типы новостей'

    def __str__(self) -> str:
        return f'{self.name}'
