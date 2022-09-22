from django.dispatch import receiver
from django.db.models.signals import pre_delete
from .models import Photo

@receiver(pre_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
    """ photo delete signal """
    instance.photo.delete(False)
