# -*- coding: utf-8 -*-
import os

from django.utils.translation import ugettext_lazy as _
from django.db                import models

from settingsDB.utils         import SettingsCached

#MODEL FOR STORING SETTINGS.PY PARAMS
class Settings(models.Model):
	name                        = models.CharField(verbose_name=_('Configuration set name'), max_length='128')
	is_enabled                  = models.BooleanField(verbose_name=_('Enable this config'), blank=True, default=False)
	
	TAGLINE                     = models.CharField(verbose_name=_('Tag line'), max_length='255', blank=True, default='')
	FOOTER                      = models.CharField(verbose_name=_('Footer sign'), max_length='255', blank=True, default='')
	
	ANONYMOUS_COMMENTS_APPROVED = models.BooleanField(verbose_name=_('Allow anonymous comments'), blank=True, default=False)
	
	# process it separately in hash (settings_local.py)
	RECAPTCHA_PUBLIC_KEY        = models.CharField(verbose_name=_('Recaptcha public key'), max_length=128, blank=True, default='')
	RECAPTCHA_PRIVATE_KEY       = models.CharField(verbose_name=_('Recaptcha private key'), max_length=128, blank=True, default='')
	
	# process it separately in hash (settings_local.py)
	GA_ACC_CODE                 = models.TextField(verbose_name=_('GoogleAnalytics code'), max_length=255, blank=True, default='')
	
	# process it separately in hash (settings_local.py)
	FEEDBURNER_NAME             = models.CharField(verbose_name=_('Your feed name in feedburner'), max_length=128, blank=True, default='')
	USE_ATOM                    = models.BooleanField(verbose_name=_('Use ATOM instead of RSS'), blank=True, default=True)
	SHORT_POSTS_IN_FEED         = models.BooleanField(verbose_name=_('Short posts in feed'), blank=True, default=True)
	
	LJ_USERNAME                 = models.CharField(verbose_name=_('LJ account username'), max_length=64, blank=True, default='')
	LJ_PASSWORD                 = models.CharField(verbose_name=_('LJ account password'), max_length=64, blank=True, default='')
	
	PAGINATE_BY                 = models.IntegerField(verbose_name=_('Blog entries per page'), blank=True, default=10)
	
	BLOG_URLCONF_ROOT           = models.CharField(verbose_name=_('Blog URL-path. Don\'t forget that there must be no leading \'/\''), max_length=64, blank='True', default='blog/')
	
	THEME = models.CharField(
		verbose_name = 'Blog templates theme',
		max_length   = 64,
		blank        = True,
		default      = 'orange',
		choices      = sorted([
			('orange'    , 'Orange'),
			('andreas08' , 'Andreas08'),
			('buriy'     , 'Buriy'),
			('catap.ru'  , 'catap.ru'),
			('lite'      , 'Lite'),
			('mirev'     , 'Mirev'),
			('web_brains', 'Web Brains'),
		]),
	)
	
	CAPTCHA = models.CharField(verbose_name='Captcha type', choices=(
		(''         , 'None'),
		('simple'   , 'Simple'),
		('recaptcha', 'Recaptcha'),
	), max_length='9', blank=True, default='')
	
	#СДЕЛАТЬ IS_ENABLED ТОЛЬКО ОДНУ ЗАПИСЬ
	def save(self):
		super(Settings, self).save()
		
		if self.is_enabled:
			for settings in Settings.objects.exclude(id=self.id):
				settings.is_enabled = False
				settings.save()
		
		return True
		
	#META
	class Meta:
		db_table            = 'settings'
		verbose_name        = u'Settings'
		verbose_name_plural = u'Settings'

models.signals.post_save.connect(SettingsCached.manage.clear, sender=Settings)
models.signals.post_delete.connect(SettingsCached.manage.clear, sender=Settings)

