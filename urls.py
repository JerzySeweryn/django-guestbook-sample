from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponsePermanentRedirect

admin.autodiscover()

urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
)

urlpatterns += patterns('',
    url(r'^guestbook/', include('guestbook.urls')),
    ('^$', lambda request: HttpResponsePermanentRedirect('/guestbook')),

)
