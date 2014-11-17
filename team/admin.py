from django.contrib import admin
from team.models import Team
from image_cropping import ImageCroppingMixin


class TeamAdmin(ImageCroppingMixin,admin.ModelAdmin):
    save_on_top = True
    list_display=  ('name','image','biography',)
    #exclude = ('cropping',)
admin.site.register(Team,TeamAdmin)