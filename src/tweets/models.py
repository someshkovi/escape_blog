from distutils.archive_util import make_zipfile
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Tweet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='tweets')
    body = models.CharField(max_length=160)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='tweets')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.body}'
