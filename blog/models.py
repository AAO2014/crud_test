from django.conf.global_settings import MEDIA_ROOT
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
