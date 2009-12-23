# -*- coding: utf-8 -*-
import memcache, MySQLdb

cache = memcache.Client(['127.0.0.1:11211'], debug=0)

#PROXY CLASS FOR CACHING SETTINGS.PY PARAMS
class SettingsCached(object):
	# cache specific methods
	class Manage(object):
		def __get__(self, inst, cls):
			return self
		
		# clear cache
		def clear(self, **kwargs):
			# http://www.djangosnippets.org/snippets/1080/
			try:
				cache.flush_all()
				
			except AttributeError:
				# try filesystem caching next
				cache._max_entries    = 0
				cache._cull_frequency = 1
				cache._cull_frequency = cache._cull_frequency
				cache._max_entries    = cache._max_entries

	# stored settings itself
	class Param(object):
		def __get__(self, inst, cls):
			return self
			
		def __getattribute__(self, name):
			import settings
			
			# в конфиге есть параметры, сформированные на основе параметров из того же конфига
			# например settings_default.THEME упоминается в settings.THEME_STATIC_URL
			# при обновлении составных частей сложных параметров их тоже надо обновлять
			# поэтому в settings сложные параметры составлены уже с использованием SettingsCached
			# и через lambda-функцию, что позволяет получать актульные данные из конфига
			
			try:
				if not cache.get(name):
					cursor    = MySQLdb.connect(
						user    = settings.DATABASE_USER,
						passwd  = settings.DATABASE_PASSWORD,
						db      = settings.DATABASE_NAME,
						charset = 'utf8'
					).cursor(MySQLdb.cursors.DictCursor)
					
					cursor.execute('SELECT * FROM settings WHERE is_enabled=1 LIMIT 1')
					
					cache.set(name, cursor.fetchall()[0][name])
			except (IndexError, KeyError):
				try:
					cache.set(name, getattr(settings, name))
				except TypeError:
					cache.set(name, getattr(settings, name)())
			
			return cache.get(name)
	
	manage = Manage()
	param  = Param()

# USAGE
#print SettingsCached.param.PAGINATE_BY
#SettingsCached.manage.clear()
