from django.db import models

# Create your models here.
class Posts(models.Model):

    author = models.CharField(max_length=50)
    postText = models.CharField(max_length=250)
    datePosted = models.DateTimeField()