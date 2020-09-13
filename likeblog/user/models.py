from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Profile(AbstractUser):
    level = models.IntegerField(default=1)
    avatar = models.ImageField(upload_to='image/avatar', blank=True)
    last_login = models.DateTimeField(auto_now=True)
