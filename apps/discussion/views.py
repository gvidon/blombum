# -*- mode: python; coding: utf-8; -*-
import datetime

from django.shortcuts import get_object_or_404
from django.http      import Http404, HttpResponseRedirect
from models           import CommentNode

#SAVE CROSSPOSTING URL RETURNED BY BLOGRESSOR
def redirect_to_view(request, id):
	try:
		comment = get_object_or_404(CommentNode, pk=int(id))
		
		if not comment.admin_view_at:
			comment.admin_view_at = datetime.datetime.today()
			comment.save()
		
		return HttpResponseRedirect('/admin/discussion/commentnode/%d/' % int(id))
	
	except ValueError:
		raise Http404

