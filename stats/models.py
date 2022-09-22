from django.db import models
from profiles.models import Profile
from simple_history.models import HistoricalRecords

class Stat(models.Model):
    """ Profile views stats """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="stats")
    views = models.PositiveIntegerField(default=0)
    history = HistoricalRecords()
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.views)
