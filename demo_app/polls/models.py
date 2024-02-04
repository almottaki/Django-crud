import datetime

from django.db import models
from django.utils import timezone
from django.db import models


class TODO(models.Model):
    text = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(default=False)


    def __str__(self):
        return self.text
