from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tag(models.Model):
    tag = models.CharField(max_length=256)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag

class File(models.Model):
    title = models.CharField(max_length=256)
    file = models.FileField(upload_to='static/files/', null=True)
    url = models.CharField(max_length=256, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)
    comments = models.CharField(max_length=512, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title