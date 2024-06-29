from django.db import models
from fiction.models import Fiction
from django.conf import settings

# Create your models here.

class Chapter(models.Model):
    fiction = models.ForeignKey(Fiction, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=200, blank=True)
    chapter_number = models.PositiveIntegerField()
    content = models.TextField(null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    view_count = models.PositiveIntegerField(default=0)
    
    class Meta:
        unique_together = ('fiction', 'chapter_number')
        ordering = ['chapter_number']
    
    def __str__(self):
        return f"{self.fiction.title}: Chapter {self.chapter_number} ({self.title})"