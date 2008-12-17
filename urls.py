from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^comments/postfree/$','publicmarkup.legislation.views.save_free_comment'),
    (r'^comments/', include('django.contrib.comments.urls.comments')),
    (r'^', include('publicmarkup.legislation.urls')),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', 'logout_then_login', name="logout"),
)

if (settings.DEBUG):
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )