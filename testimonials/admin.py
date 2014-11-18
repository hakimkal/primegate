from django.contrib import admin
from testimonials.models import Testimonial
from image_cropping import ImageCroppingMixin


class TestimonialAdmin(ImageCroppingMixin,admin.ModelAdmin):
    save_on_top = True
    list_display=  ('name','image','remark','created', 'modified')
    #exclude = ('cropping',)
admin.site.register(Testimonial,TestimonialAdmin)