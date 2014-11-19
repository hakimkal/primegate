from django.db import models
from image_cropping import ImageRatioField

class Homepagebanner(models.Model):
    image = models.ImageField(upload_to='banners_images')
    # size is "width x height"
    cropping = ImageRatioField('image', '1110x640')
    caption = models.CharField(max_length=200)
    url= models.URLField(blank=True, null= True)
    brief_info =  models.TextField(null=True, blank=True)