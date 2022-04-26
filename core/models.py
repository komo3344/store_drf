from django.db import models


class VisibleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_hidden=False)


class DateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VisibleDateTimeModel(DateTimeModel):
    objects = models.Manager()
    visible_objects = VisibleManager()

    class Meta:
        abstract = True
        base_manager_name = 'objects'
