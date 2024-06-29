from django.db import models

from fiction.models import Fiction

class Category(models.Model):
    name = models.CharField(max_length=200)
    fictions = models.ManyToManyField(Fiction, blank=True)
    
    def __str__(self):
        return self.name[:50]
