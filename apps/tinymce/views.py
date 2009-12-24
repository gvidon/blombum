import re

from django.shortcuts import render_to_response
from django.template  import RequestContext
from django.http      import Http404, HttpResponseRedirect

from settingsDB.utils import SettingsCached

def read_path(request, path):
	if re.search('(jpg|png|jpeg|gif)$', path):
		return HttpResponseRedirect(SettingsCached.param.STATIC_URL+'js/tinymce/'+path)
	
	return render_to_response('tinymce/'+path, RequestContext(request))
