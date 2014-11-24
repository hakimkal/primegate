from django.contrib import admin
from image_cropping import ImageCroppingMixin
from news.models import News
 



class NewsAdmin(ImageCroppingMixin,admin.ModelAdmin):
    save_on_top = True
    list_display= ('caption','story','image','created', 'modified', 'tags')
    exclude = ('user',)
    
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
    
        
admin.site.register(News, NewsAdmin)
