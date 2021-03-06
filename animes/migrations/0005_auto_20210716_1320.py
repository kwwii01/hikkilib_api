# Generated by Django 3.2.5 on 2021-07-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0004_auto_20210716_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=500, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='seiyu',
            name='year_of_birth',
            field=models.DateField(null=True, verbose_name='Year of birth'),
        ),
    ]
