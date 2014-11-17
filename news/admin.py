
from news.models import News
 
from django.contrib import admin


class NewsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display= ('caption','story','image','created', 'modified', 'tags')
    exclude = ('user',)
    
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
    
        
admin.site.register(News, NewsAdmin)
