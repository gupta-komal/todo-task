from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.

class AdditionalInfo(models.Model):
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    class Meta:
        abstract = True

class Task(AdditionalInfo):
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline_date = models.DateField()

