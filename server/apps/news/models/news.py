from django.db import models

from .managers import NewsManager


class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок новости',
    )
    short_description = models.TextField(
        verbose_name='Краткое описание'
    )
    full_description = models.TextField(
        verbose_name='Полное описание'
    )
    type = models.ForeignKey(
        to='news.NewsType',
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name='Тип новости'
    )

    objects = NewsManager()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self) -> str:
        return f'{self.title}'
