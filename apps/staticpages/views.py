from django.shortcuts import get_object_or_404
from lib.decorators   import render_to
from models           import StaticPage

@render_to('staticpages/default.html')
def page(request, slug):
	return {'flatpage': get_object_or_404(StaticPage, url=slug)}
