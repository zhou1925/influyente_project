from django.db import models
from django.contrib.auth import get_user_model
from .utils import reduce_size, add_watermark


User = get_user_model()

class Photo(models.Model):
    """ Photo model of user """
    photo = models.ImageField(upload_to='photos/%Y/%m/%d') 
    user = models.ForeignKey(User, related_name="photos", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        if self.photo:
            reduce_size(self.photo.path)
            add_watermark(self.photo.path)
    
