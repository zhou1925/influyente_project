from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Boost


@receiver(post_save, sender=Boost)
def save_boost(sender, instance, created, **kwargs):
    """ save boost signal to update the boost and create a timmer """
    if created:
        boost = instance
        boost.profile.last_boost_type = boost.boostType.name
        boost.profile.isBoost = True
        boost.profile.save()
        profile_id = boost.profile.id
        timeHrs = boost.boostType.timeHrs
        timeLeft2 = timeHrs * 3600 * 1
        timeLeft = 60*3
        from .tasks import update_isBoost
        update_isBoost.apply_async(kwargs={'profile_id':profile_id}, countdown=timeLeft)
        
