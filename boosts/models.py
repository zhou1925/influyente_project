from django.db import models
from cacheops import invalidate_model
from profiles.models import Profile

class Boost(models.Model):
    """ Boost model """
    profile = models.ForeignKey(Profile, related_name="boosts", on_delete=models.CASCADE) 
    boostType = models.ForeignKey("BoostType", related_name="boost_type", on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.user.username + f"have boost: {self.boostType.name}"

# invalidate model to avoid cache
invalidate_model(Boost)

class BoostType(models.Model):
    """ Boost Type """
    name = models.CharField(max_length=1)
    timeHrs = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
