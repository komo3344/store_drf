from django.db import models
from core import models as core_models


class Vendor(core_models.DateTimeModel):
    owner = models.OneToOneField('api.User', on_delete=models.CASCADE, related_name='vendor')
    name = models.CharField(max_length=30)
    desc = models.TextField(default='', blank=True)
