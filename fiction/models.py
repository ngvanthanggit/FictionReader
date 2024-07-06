from django.db import models
from django.conf import settings
from genre.models import Genre

# Create your models here.

class Fiction(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=250)
    about = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    poster = models.ImageField(null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    def short_brief(self):
        return f"{self.about[:150]}..."