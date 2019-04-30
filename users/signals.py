##AUTOMATICALLY CREATES A PROFILE IF A USER SIGNS UP

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

##basically bloche, if user is created, create a profile for the user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created :
        Profile.objects.create(user=instance)

##basically bolche, create howar por save o hote hobe
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()