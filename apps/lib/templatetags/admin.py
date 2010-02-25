# -*- mode: python; coding: utf-8; -*-

from django.contrib.auth.models import User
from django.template            import Library

from discussion.models          import CommentNode
from blog.models                import Post

register = Library()

@register.simple_tag
def posts_count():
    return Post.objects.all().count()

@register.simple_tag
def comments_count():
    return CommentNode.objects.filter(approved=1).count()

@register.inclusion_tag('templatetags/admin/new_comments.html')
def new_comments():
    return { 'comments': CommentNode.objects.filter(admin_view_at=None).order_by('-upd_date') }
