from django.db import models
from image_cropping import ImageRatioField

class Team(models.Model):
    image = models.ImageField(upload_to='team_images')
    # size is "width x height"
    cropping = ImageRatioField('image', '100x100')
    name = models.CharField(max_length=100)
    biography= models.TextField()
    designation =  models.CharField(max_length=255,default='Staff')