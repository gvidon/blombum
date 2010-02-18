# -*- mode: python; coding: utf-8; -*-
import json
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
		
		crosspost.save()
		
		return HttpResponse('{ postid: %d, serviceid: %d }' % (crosspost.post.id, crosspost.service.id))
	
	except KeyError:
		raise Http404

#RETURN CROSSPOSTING URLS FOR ENTRY
def urls(request, id):
	#!!WARN!!: тут еще отправлять инфу о том - закончен
	#кросспостинг поста или нет и когда
	return HttpResponse(json.dumps({ 'urls': [C.url for C in Crosspost.objects.filter(post=id)] }))


