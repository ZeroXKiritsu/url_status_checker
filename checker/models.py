from django.db import models
from django.db.models.base import Model

# Create your models here.
class URL(models.Model):
    url = models.URLField(max_length=200, unique=True, verbose_name="URL")
    status = models.IntegerField(null=True, verbose_name="status")
    check_interval = models.PositiveIntegerField(default=5, verbose_name="check interval")
    
    is_paused = models.BooleanField(default=False, verbose_name="paused")

    def __str__(self):
        return self.url