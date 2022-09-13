from django.db.models import Manager

from ..querysets import NewsTypeQuerySet


class NewsTypeManager(Manager):
    def get_queryset(self, **kwargs) -> NewsTypeQuerySet:
        return NewsTypeQuerySet(
            self.model,
            using=self.db,
        )
