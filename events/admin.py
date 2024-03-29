from django.contrib import admin
from image_cropping import ImageCroppingMixin
from events.models import Event


class EventAdmin(ImageCroppingMixin,admin.ModelAdmin):
    save_on_top = True
    list_display= ('caption','event_details','image','created','start_date','end_date', 'modified', 'tags')
    exclude = ('user',)
    
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
    
        
admin.site.register(Event, EventAdmin)
