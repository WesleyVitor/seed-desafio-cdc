from django.db import models
from django.contrib.auth.models import *
from datetime import datetime
# Create your models here.

class Author(models.Model):
    """
    Guarda informações sobre autores
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
