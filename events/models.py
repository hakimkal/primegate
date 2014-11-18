from django.db import models
from image_cropping import ImageRatioField


from django.contrib.auth import get_user_model
from datetime import datetime

class Event(models.Model):
    
    #ImageField(upload_to=None[, height_field=None, width_field=None, max_length=100, **options])
    image = models.ImageField(upload_to = 'events_images/',default = 'events_images/None/no-img.jpg')
    caption = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.now(),auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(default=datetime.now(),auto_now=True, auto_now_add=False)
    start_date = models.DateTimeField()
    synopsis = models.CharField(max_length=20,blank=True)
    end_date = models.DateTimeField()
    event_details = models.TextField(blank= True)
    tags = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model())
    cropping = ImageRatioField('image', '246x246')
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural ='Events'
    
    
    def __unicode__(self):
        return self.caption