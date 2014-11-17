from django.db import models
from datetime import datetime
# Create your models here.
class Nlsubscriber(models.Model):
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=60, blank=True)
    lastname = models.CharField(max_length=60,blank=True)
    created = models.DateTimeField(default=datetime.now(),auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(default=datetime.now(),auto_now=True, auto_now_add=False)
    class Meta:
        
        verbose_name = 'Newsletter Subscription list'
        verbose_name_plural ='Newsletter Subscription'
        
    
    
    
    def __unicode__(self):
        return self.email