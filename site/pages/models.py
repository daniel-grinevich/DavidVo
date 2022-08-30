from pydoc import describe
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = HTMLField(blank=True)
    feature_image = models.ImageField(blank=True)
    rank = models.IntegerField(default=0)
    is_in_navigation = models.BooleanField(default=True)
    navigation_title = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.navigation_title

    class Meta: 
        ordering = ('-rank','pk')
    