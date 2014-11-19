from django.db import models
from image_cropping import ImageRatioField
from datetime import datetime
class Testimonial(models.Model):
    image = models.ImageField(upload_to='team_images')
    # size is "width x height"
    cropping = ImageRatioField('image', '200x200')
    name = models.CharField(max_length=100)
    remark= models.TextField()
    designation =  models.CharField(max_length=255,default='Parent')
    created = models.DateTimeField(default=datetime.now(),auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(default=datetime.now(),auto_now=True, auto_now_add=False)