# -*- mode: python; coding: utf-8; -*-

import re
from datetime import datetime as dt

from django.template import Library

from discussion.models import CommentNode
from blog.models import Post
from lib.db import load_content_objects

register = Library()

@register.inclusion_tag('blog/sidebar.html', takes_context=True)
def sidebar(context):
    all_posts = Post.objects.filter(date__lte=dt.now()).order_by('-date')
    
    #FIXED 24.12.2009
    try:
        comments = CommentNode.objects.for_similar_objects(all_posts)
        comments = comments.select_related().order_by('-pub_date')[:5]
    
    #FIXED 24.12.2009
    except AttributeError:
        comments = []
     
    last_posts = all_posts[:5]
    # TODO: return all variables from RequestContext dictionary
    return {
            'STATIC_URL': context['STATIC_URL'],
            'request': context['request'],
            'last_posts': last_posts,
            'settings': context['settings'],
            'comments': comments,
            }
