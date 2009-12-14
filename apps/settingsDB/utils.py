from django.core.cache import cache
from models            import Settings

#PROXY CLASS FOR CACHING SETTINGS.PY PARAMS
class SettingsCached(object):

	#PROVIDE STATIC ATTRIBUTES AND METHODS
	class Param(object):
		def __get__(self, inst, cls):
			return self
			
		def __getattribute__(self, name):
			print cache.get(name, 'asd')
			return cache.get(name, 'asd')
	
	param = Param()

# USAGE
# print SettingsCached.param.PAGINATE_BY
