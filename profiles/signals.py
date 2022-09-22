from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import Profile
from stats.models import Stat


User = get_user_model()

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """ Profile, Stat  when user is created """
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()
        stat = Stat(profile=profile)
        stat.save()
