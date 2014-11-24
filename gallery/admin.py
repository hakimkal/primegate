from django.contrib import admin
from image_cropping import ImageCroppingMixin
from gallery.models import Gallery

class GalleryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display=('image','caption')
    #exclude =('cropping','thumb')

admin.site.register(Gallery,GalleryAdmin)