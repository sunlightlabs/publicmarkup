from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from publicmarkup.legislation.views import Index

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^about/$', 'publicmarkup.views.about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/postfree/$','publicmarkup.legislation.views.save_free_comment'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^comments/', Index.as_view()),
    url(r'^contact/$', 'publicmarkup.views.contact'),
    url(r'^signup/$', 'publicmarkup.views.signup'),
    url(r'^', include('publicmarkup.legislation.urls')),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', 'logout_then_login', name="logout"),
)