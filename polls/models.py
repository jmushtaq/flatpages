from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

class Polls(models.Model):
    name        = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)




