# -*- mode: python; coding: utf-8; -*-
from django.template         import Library
from apps.staticpages.models import StaticPage

register = Library()

@register.inclusion_tag('templatetags/staticpages.html', takes_context=True)
def staticpages_links(context):
	return {'pages': StaticPage.objects.all(), 'page_url': context['request'].path}
