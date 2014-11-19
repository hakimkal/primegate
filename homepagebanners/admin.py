from django.contrib import admin
from homepagebanners.models import Homepagebanner

class HomepagebannerAdmin(admin.ModelAdmin):
    list_display=('image','caption','brief_info','url')

admin.site.register(Homepagebanner,HomepagebannerAdmin)