from django.conf.urls.defaults import *

urlpatterns = patterns('guestbook.views',
    (r'^$', 'index'),
    (r'^(?P<com_id>\d+)/$', 'detail'),
    (r'^add/', 'add'),
    (r'^search/', 'search'),
)
