# -*- mode: python; coding: utf-8; -*-

from django.utils.translation import ugettext_lazy as _
from django.db                import models

class StaticPage(models.Model):
	url     = models.CharField(_('URL'), max_length=100, db_index=True)
	title   = models.CharField(_('title'), max_length=200)
	content = models.TextField(_('content'), blank=True)
		
	def __unicode__(self):
		return u"%s - %s" % (self.url, self.title)
	
	def get_absolute_url(self):
		return self.url

	class Meta:
		db_table            = 'static_page'
		verbose_name        = _('static page')
		verbose_name_plural = _('static pages')
		ordering            = ('url',)
