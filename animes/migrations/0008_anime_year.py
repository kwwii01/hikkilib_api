# Generated by Django 3.2.5 on 2021-07-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0007_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='year',
            field=models.PositiveIntegerField(default=2021, verbose_name='Year'),
        ),
    ]