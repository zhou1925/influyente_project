from celery.utils.log import get_task_logger
from celery import Celery
from celery import shared_task
from .models import Profile

app = Celery()

logger = get_task_logger(__name__)

@shared_task
def update_isBoost(**kwargs):
    """ update boost of profile """
    profile_id = kwargs['profile_id']
    profile = Profile.objects.get(pk=profile_id)
    profile.isBoost = False
    profile.save()

