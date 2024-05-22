from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=122)
    author = models.CharField(max_length=122)
    content_markdown = models.TextField(default="")
    image = models.ImageField(upload_to='blog/images')
