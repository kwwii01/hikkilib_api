from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import Profile, AnimeListItem, AnimeList


@receiver(post_save, sender=User)
def create_profile_and_list(sender, instance, created, **kwargs):
    if created:
        p = Profile.objects.create(user=instance)
        AnimeList.objects.create(profile=p)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created is False:
        instance.profile.save()


@receiver(post_save, sender=AnimeListItem)
def update_rating(sender, instance, created, **kwargs):
    anime = instance.anime
    anime.rating = anime.calculate_rating()
    anime.save()
