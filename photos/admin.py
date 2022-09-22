from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']
    
admin.site.register(Photo, PhotoAdmin)
