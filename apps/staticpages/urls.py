# -*- mode: python; coding: utf-8; -*-

from django.conf.urls.defaults import *
from views                     import page

urlpatterns = patterns('',
	url(r'(?P<slug>[-\w]+)/?$', page, name='staticpage'),
)
