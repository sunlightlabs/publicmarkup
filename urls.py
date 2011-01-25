from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/postfree/$','publicmarkup.legislation.views.save_free_comment'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^comments/', 'publicmarkup.legislation.views.index'),
    url(r'^contact/$', 'publicmarkup.views.contact'),
    url(r'^signup/$', 'publicmarkup.views.signup'),
    url(r'^', include('mediasync.urls')),
    url(r'^', include('publicmarkup.legislation.urls')),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^about/$', 'direct_to_template', {'template': 'about.html'}),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', 'logout_then_login', name="logout"),
)