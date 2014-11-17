from django.conf.urls import patterns, include, url
import publicpages.views
import nlsubscribers.views
import news.views
import events.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'primegate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
   
    url(r'^$', publicpages.views.index, name="home"),
    url(r'^about/$', publicpages.views.about, name='about'),
    url(r'^contact/$', publicpages.views.contact, name = 'contact'),
    url(r'^team/$', publicpages.views.team, name = 'team'),
    url(r'^nladd',nlsubscribers.views.nladd, name = "nladd"),
    url(r'^news/$',news.views.index,name='news'),
    url(r'^events/$',events.views.index, name="events"),
    url(r'^admin/', include(admin.site.urls)),
)
