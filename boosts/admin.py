from django.contrib import admin
from .models import Boost, BoostType

@admin.register(Boost)
class BoostAdmin(admin.ModelAdmin):
    list_display = ['profile', 'boostType']

@admin.register(BoostType)
class BoostTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'timeHrs', 'price']
