from django.db import models


class Seiyu(models.Model):
    name = models.CharField('Name', max_length=100)
    picture = models.ImageField('Picture', upload_to='seiyu/')
    url = models.SlugField(unique=True, max_length=160)

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField('Name', max_length=100)
    picture = models.ImageField('Picture', upload_to='producers/')
    url = models.SlugField(unique=True, max_length=160)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField('Name', max_length=100)
    picture = models.ImageField('Picture', upload_to='characters/')
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    description = models.CharField('Description', max_length=1500)
    seiyu = models.ForeignKey(Seiyu, on_delete=models.SET_NULL, blank=True,
                              related_name='voiced_characters', null=True)
    url = models.SlugField(unique=True, max_length=160)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Name', max_length=40, unique=True)
    description = models.CharField('Description', max_length=200)
    url = models.SlugField(unique=True, max_length=160)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField('Name', max_length=40, unique=True)
    url = models.SlugField(unique=True, max_length=160)

    def __str__(self):
        return self.name


class Anime(models.Model):
    STATUS_CHOICES = [
        ('anons', 'Announced'),
        ('air', 'Airing'),
        ('fin', 'Finished')
    ]
    title = models.CharField('Title', max_length=100)
    poster = models.ImageField('Poster', upload_to='anime_posters/')
    description = models.CharField('Description', max_length=1500)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=5)
    release_date = models.DateField('Release date')
    genres = models.ManyToManyField(Genre)
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, blank=True, null=True)
    url = models.SlugField(unique=True, max_length=160)
