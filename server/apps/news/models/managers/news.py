from django.db.models import Manager

from ..querysets import NewsQuerySet


class NewsManager(Manager):
    def get_queryset(self, **kwargs) -> NewsQuerySet:
        return NewsQuerySet(
            self.model,
            using=self.db,
        )
