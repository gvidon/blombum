# -*- mode: python; coding: utf-8; -*-

from django.conf.urls.defaults import *
from views                     import read_path

# use VERY carefully
urlpatterns = patterns('',
	url(r'(?P<path>[\w\d_/\-\.]+\.(jpg|jpeg|png|gif|css|js|html?)+)$', read_path, name='tinymce-files'),
)
