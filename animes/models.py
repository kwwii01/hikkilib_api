from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Profile(models.Model):
    SEX_CHOICE = [
        ('f', 'Female'),
        ('m', 'Male'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField('Picture', upload_to='profiles/', null=True, blank=True,
                                default='profiles/nopic.png')
    sex = models.CharField('Sex', choices=SEX_CHOICE, max_length=1, null=True, blank=True)
    bio = models.TextField('Bio', max_length=500, null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_age_or_question_mark(self):
        if self.birth_date is None:
            return '?'

        today = date.today()
        birth = self.birth_date
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))


class Seiyu(models.Model):
    name = models.CharField('Name', max_length=100)
    picture = models.ImageField('Picture', upload_to='seiyu/')
    year_of_birth = models.DateField('Year of birth', auto_now=False, blank=False, null=True)
    year_of_death = models.DateField('Year of death', auto_now=False, blank=True, null=True)
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
    description = models.TextField('Description')
    seiyu = models.ForeignKey(Seiyu, on_delete=models.SET_NULL, blank=True,
                              related_name='voiced_characters', null=True)
    url = models.SlugField(unique=True, max_length=160)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Name', max_length=40, unique=True)
    description = models.TextField('Description', max_length=500)
    url = models.SlugField(unique=True, max_length=160)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField('Name', max_length=40, unique=True)
    url = models.SlugField(unique=True, max_length=160)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField('Name', max_length=15, unique=True)
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
    description = models.TextField('Description')
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    rating = models.FloatField('Rating', default=0, null=True)
    year = models.PositiveIntegerField('Year', default=2021)
    release_date = models.DateField('Release date')
    genres = models.ManyToManyField(Genre)
    characters = models.ManyToManyField(Character)
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, blank=True, null=True)
    url = models.SlugField(unique=True, max_length=160)

    def __str__(self):
        return self.title

    def calculate_rating(self):
        ratings_count = self.users_ratings.all().count()
        if ratings_count == 0:
            return 0

        score_sum = 0
        for rating in self.users_ratings.all():
            score_sum += rating.score
        return round((score_sum / ratings_count), 2)


class Comment(models.Model):
    text = models.TextField('Text', max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='comments')
    publish_date = models.DateTimeField('Publish date', auto_now=True)

    def __str__(self):
        return f"{self.user.username} about {self.anime} ({str(self.publish_date)})"


class AnimeScreenshots(models.Model):
    screenshot = models.ImageField('Screenshot', upload_to='anime_screenshots/')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='anime_screenshots')


class Rating(models.Model):
    WORST = 1
    TERRIBLE = 2
    SHITTY = 3
    BAD = 4
    SOSO = 5
    FINE = 6
    GOOD = 7
    EXCELLENT = 8
    MASTERPIECE = 9
    GODTIER = 10
    SCORE_CHOICES = [
        (WORST, 'Worst'),
        (TERRIBLE, 'Terrible'),
        (SHITTY, 'Shitty'),
        (BAD, 'Bad'),
        (SOSO, 'So-so'),
        (FINE, 'Fine'),
        (GOOD, 'Good'),
        (EXCELLENT, 'Excellent'),
        (MASTERPIECE, 'Masterpiece'),
        (GODTIER, 'God tier')
    ]
    score = models.IntegerField('Score', choices=SCORE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='users_ratings')

    def __str__(self):
        return f"{self.user.username} rated {self.anime.title} with {self.score}"
