from django.db import models


# Create your models here.
class Post(models.Model):
    creator = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=160)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    icon = models.ImageField(upload_to='image/icon')


class Theme(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=160)
    text = models.TextField()
    icon = models.ImageField(upload_to='image/icon')
    posts = models.ManyToManyField(Post)
