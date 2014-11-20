from django.db import models
from image_cropping import ImageRatioField
import datetime
class Gallery(models.Model):
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        
    image = models.ImageField(upload_to='gallery_images')
    # size is "width x height"
    cropping = ImageRatioField('image', '1600x1066')
    thumb = ImageRatioField('image', '200x200')
    caption = models.CharField(max_length=200,null=True, blank=True)
    created = models.DateTimeField(default =datetime.datetime.now(), auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(default=datetime.datetime.now(),auto_now=True, auto_now_add=False)
    
    