# Generated by Django 2.0.3 on 2018-04-03 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0009_album_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='likes',
        ),
    ]