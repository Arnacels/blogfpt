from django.db import models


# Create your models here.
class Post(models.Model):
    creator = models.ForeignKey('user.Profile', on_delete=models.CASCADE, related_name='creator')
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=160)
    text = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0, blank=True)
    likes = models.IntegerField(default=0, blank=True)
    likes_user = models.ManyToManyField('user.Profile')
    icon = models.ImageField(upload_to='image/icon')


class Theme(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=160)
    posts = models.ManyToManyField(Post)
