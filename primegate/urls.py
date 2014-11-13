from django.conf.urls import patterns, include, url
import publicpages.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'primegate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', publicpages.views.index, name="home"),
    url(r'^about$', publicpages.views.about, name='about'),
    url(r'^contact$', publicpages.views.contact, name = 'contact'),
    url(r'^team$', publicpages.views.team, name = 'team')
)
