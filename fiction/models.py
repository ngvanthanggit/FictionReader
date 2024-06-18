from django.db import models

# Create your models here.

class Fiction(models.Model):
    #author =
    name = models.CharField(max_length=250)
    story = models.TextField(null=True, blank=True)
    poster = models.ImageField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)