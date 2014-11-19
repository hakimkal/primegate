from django.db import models
from django.contrib.auth import get_user_model
from image_cropping import ImageRatioField
from datetime import datetime
class News(models.Model):
    class Meta:
        verbose_name = 'News'
        verbose_name_plural ='News'
    #ImageField(upload_to=None[, height_field=None, width_field=None, max_length=100, **options])
    image = models.ImageField(upload_to = 'news_images/',default = 'news_images/None/no-img.jpg')
    caption = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.now(),auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(default=datetime.now(),auto_now=True, auto_now_add=False)
    story = models.TextField(blank= True)
    tags = models.CharField(max_length=255)
    cropping = ImageRatioField('image', '772x514')
    user = models.ForeignKey(get_user_model())
    
    
    def __unicode__(self):
        return self.caption