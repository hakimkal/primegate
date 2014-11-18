from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

import publicpages.views
import nlsubscribers.views
import news.views
import events.views
import faqs.views
import team.views
import testimonials.views
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
    url(r'^events/$',events.views.index, name="event_listing"),
    url(r'^events/(?P<id>\d+)/$',events.views.detail, name="event"),
    url(r'^teams/$',team.views.index, name="theteam"),
    url(r'faq/$',faqs.views.index, name="faqs"),
    url(r'^testimonials/$',testimonials.views.index, name="testimonials"),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
