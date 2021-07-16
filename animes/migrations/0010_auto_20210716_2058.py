# Generated by Django 3.2.5 on 2021-07-16 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0009_auto_20210716_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='animes',
        ),
        migrations.AddField(
            model_name='anime',
            name='characters',
            field=models.ManyToManyField(to='animes.Character'),
        ),
    ]
