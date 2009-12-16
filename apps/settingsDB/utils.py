from django.core.cache import cache
from django.conf       import settings

from models            import Settings

#PROXY CLASS FOR CACHING SETTINGS.PY PARAMS
class SettingsCached(object):

	#PROVIDE STATIC ATTRIBUTES AND METHODS
	class Param(object):
		def __get__(self, inst, cls):
			return self
			
		def __getattribute__(self, name):
			try:
				if not cache.get(name):
					cache.set(name, Settings.objects.get(is_enabled=True).values(name))
				
			except Settings.DoesNotExist:
				cache.set(name, getattr(settings, name))
				
			return cache.get(name)
			
	param = Param()

# USAGE
#print SettingsCached.param.PAGINATE_BY
