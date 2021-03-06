# Generated by Django 2.0.3 on 2018-03-30 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='favorite',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musics.Album'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
