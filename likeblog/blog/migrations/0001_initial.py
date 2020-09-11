# Generated by Django 3.1.1 on 2020-09-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=160)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('icon', models.ImageField(upload_to='image/icon')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=160)),
                ('text', models.TextField()),
                ('icon', models.ImageField(upload_to='image/icon')),
                ('posts', models.ManyToManyField(to='blog.Post')),
            ],
        ),
    ]
