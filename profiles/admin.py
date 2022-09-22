from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'isBoost', 'last_boost_type', 'active', 'location']

admin.site.register(Profile, ProfileAdmin)
