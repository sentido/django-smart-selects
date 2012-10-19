
from django.conf.urls import patterns, url

from . import settings
from .views import filterchain, filterchain_all

if settings.AUTH_DECORATOR:
    filterchain = settings.AUTH_DECORATOR(filterchain)
    filterchain_all = settings.AUTH_DECORATOR(filterchain_all)

urlpatterns = patterns('smart_selects.views',
    url(r'^all/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<field>[\w\-]+)/(?P<value>[\w\-]+)/$', filterchain_all, name='chained_filter_all'),
    url(r'^filter/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<field>[\w\-]+)/(?P<value>[\w\-]+)/$', filterchain, name='chained_filter'),
)
