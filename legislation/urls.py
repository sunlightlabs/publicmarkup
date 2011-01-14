from django.conf.urls.defaults import *
from publicmarkup.legislation.models import Legislation
from publicmarkup.legislation.feeds import LegislationComments

index_dict = {
    'queryset': Legislation.objects.all().order_by("-id")
}

feeds = {
    "comments": LegislationComments,
}

urlpatterns = patterns('publicmarkup.legislation.views',
    url(r'^$', 'index', index_dict, name="index"),
    url(r'^bill/$', 'bill', name='bill'),
    url(r'^bill/(?P<legislation_slug>[-\w]+)/$', 'legislation_detail', name='legislation_detail'),
    url(r'^bill/(?P<legislation_slug>[-\w]+)/print/$', 'legislation_print', name='legislation_print'),
    url(r'^bill/(?P<legislation_slug>[-\w]+)/(?P<title_num>\d+)/$', 'title_detail', name='title_detail'),
    url(r'^bill/(?P<legislation_slug>[-\w]+)/(?P<title_num>\d+)/(?P<section_num>\d+)/$', 'section_detail', name='section_detail'),
)

urlpatterns += patterns('django.contrib.syndication.views',
    url(r'^feed/(?P<url>.*)/$', 'feed', {'feed_dict': feeds}),
)