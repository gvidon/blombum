# -*- mode: python; coding: utf-8; -*-
try:
	from json import dumps
except ImportError:
	from json import write as dumps

from datetime         import datetime

from django.shortcuts import get_object_or_404
from django.http      import Http404, HttpResponse

from blog.models      import Post
from models           import Crosspost

#SAVE CROSSPOSTING URL RETURNED BY BLOGRESSOR
def catch(request, code):
	crosspost = get_object_or_404(Crosspost, code=code, finished_at=None, url=None)
	
	try:
		crosspost.finished_at = datetime.today()
		crosspost.url         = request.POST['url']
		
		crosspost.error_code  = request.POST.get('error', '')
		crosspost.error_stage = request.POST.get('error_stage', '')
		
		crosspost.save()
		
		return HttpResponse('{ postid: %d, serviceid: %d }' % (crosspost.post.id, crosspost.service.id))
	
	except KeyError:
		raise Http404

#RETURN CROSSPOSTING URLS FOR ENTRY
def urls(request, id):
	#!!WARN!!: тут еще отправлять инфу о том - закончен
	#кросспостинг поста или нет и когда
	return HttpResponse(dumps([{
		'service': C.service.name,
		'error'  : C.error_code,
		'date'   : C.finished_at and C.finished_at.strftime("%d %B %Y") or None,
		'url'    : C.url,
	} for C in Crosspost.objects.filter(post=id).order_by('service')]))


