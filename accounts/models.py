from django.db import models
from django.contrib.auth.models import AbstractUser

from fiction.models import Fiction
from chapter.models import Chapter

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100, blank=False)
    avatar = models.ImageField(null=True, default="avatar_new.png")
    wallpaper = models.ImageField(null=True, default="wallpaper_default.jpeg")
    
    ongoing_chapters = models.ManyToManyField(Chapter, related_name="ongoing_fictions", blank=True)
    finished_fictions = models.ManyToManyField(Fiction, related_name="finished_fictions", blank=True)
    favorite_fictions = models.ManyToManyField(Fiction, related_name="favorite_fictions", blank=True)
    
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username
