from django.contrib import admin
from image_cropping import ImageCroppingMixin

from homepagebanners.models import Homepagebanner
#ImageCroppingMixin, admin.ModelAdmin
class HomepagebannerAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display=('image','caption','brief_info','url')

admin.site.register(Homepagebanner,HomepagebannerAdmin)