# -*- coding: utf-8; -*-
from django.conf.urls.defaults import *
from views                     import catch, urls

urlpatterns = patterns('',
	url(r'urls/(?P<id>[\d]+)/?$', urls , name='crosspost-urls'),
	url(r'(?P<code>[\w\d]+)/?$' , catch, name='catch-url'),
)
