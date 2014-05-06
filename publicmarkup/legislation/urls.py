from django.conf.urls import patterns, url
from publicmarkup.legislation.feeds import LegislationComments
from publicmarkup.legislation.models import Legislation
from publicmarkup.legislation.views import Index, legislation_detail, legislation_print, title_detail, section_detail

feeds = {
    "comments": LegislationComments,
}

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name="index"),
    url(r'^bill/$', 'bill', name='bill'),
    url(r'^bill/(?P<legislation_slug>[-\w]+)/$', legislation_detail, name='legislation_detail'),
    url(r'^bill/(?P<legislation_slug>[-\w]+)/print/$', legislation_print, name='legislation_print'),
    url(r'^bill/(?P<legislation_slug>[-\w]+)/(?P<title_num>\d+)/$', title_detail, name='title_detail'),
    url(r'^bill/(?P<legislation_slug>[-\w]+)/(?P<title_num>\d+)/(?P<section_num>\d+)/$', section_detail, name='section_detail'),
    url(r'^feed/comments/$', LegislationComments()),
)
