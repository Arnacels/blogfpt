from django.contrib import admin
from .models import Theme, Post

# Register your models here.
admin.site.register((Theme, Post))