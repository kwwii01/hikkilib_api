# Generated by Django 3.2.5 on 2021-07-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
    ]
