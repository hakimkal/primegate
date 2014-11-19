from django.contrib import admin
from gallery.models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display=('image','caption')
    exclude =('cropping','thumb')

admin.site.register(Gallery,GalleryAdmin)