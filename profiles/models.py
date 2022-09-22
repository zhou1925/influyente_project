from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Location(models.TextChoices):
    HUAMANGA = 'HUAMANGA'
    HUANCA_SANCOS = 'HUANCA_SANCOS'
    HUANTA = 'HUANTA'
    LA_MAR = 'LA_MAR'
    LUCANAS = 'LUCANAS'
    PARINACOCHAS = 'PARINACOCHAS'
    SUCRE = 'SUCRE'
    VICTOR_FAJARDO = 'VICTOR_FAJARDO'
    VILCAS_HUAMAN = 'VILCAS_HUAMAN'
    PAUCAR_DEL_SARA_SARA = 'PAUCAR_DEL_SARA_SARA'

class Genere(models.TextField):
    MALE = 'MALE'
    FEMALE = 'FEMALE'

class Profile(models.Model):
    """ user one to one profile"""
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    isBoost = models.BooleanField(default=False, db_index=True)
    verified = models.BooleanField(default=False)
    last_boost_type = models.CharField(max_length=1, null=True, db_index=True)
    active = models.BooleanField(default=True, db_index=True)
    location = models.CharField(choices=Location.choices, max_length=30, default=Location.HUAMANGA, db_index=True)
    age = models.PositiveIntegerField(null=True, db_index=True)
    photo = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.user.username
    
    @property
    def last_boost(self):
        if self.boosts.last() == None:
            return None
        else:
            return self.boosts.last().boostType.name
