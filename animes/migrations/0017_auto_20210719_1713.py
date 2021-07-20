# Generated by Django 3.2.5 on 2021-07-19 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0016_auto_20210718_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='rating',
            field=models.FloatField(default=0, null=True, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='animescreenshots',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anime_screenshots', to='animes.anime'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='profiles/nopic.png', null=True, upload_to='profiles/', verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_ratings', to='animes.anime'),
        ),
    ]