from django.utils.translation import ugettext_lazy as _
from django.db                import models

#SIDE SERVICE DESCRIPTION WITH SPECIFIC USER DATA
class SideService(models.Model):
	name     = models.CharField(_(u'Account name'), max_length=128)
	url      = models.CharField(_(u'Your page URL'), max_length=128, blank=True)
	
	login    = models.CharField(_(u'Login'), max_length=128)
	password = models.CharField(_(u'Password'), max_length=64)
	
	type  = models.CharField(_(u'Name'), choices=(
		('blogger', 'Blogger.com'),
		('twitter', 'Twitter'),
	), max_length=32)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table            = 'sideservice'
		verbose_name        = _('Side service')
		verbose_name_plural = _('Side services')

#CROSSPOSTING PROCESS STATUS
class Crosspost(models.Model):
	post        = models.ForeignKey('blog.Post', verbose_name=_(u'Post'), related_name='crossposts')
	service     = models.ForeignKey('SideService', verbose_name=_(u'Service name'))
	
	started_at  = models.DateTimeField(_(u'Process start time'), blank=True, null=True)
	finished_at = models.DateTimeField(_(u'Process finish time'), blank=True, null=True)
	
	error_code  = models.CharField(_(u'Error code'), max_length=8, blank=True, null=True)
	error_stage = models.CharField(_(u'Error stage'), max_length=8, blank=True, null=True)
	
	url         = models.CharField(_(u'Crosspost URL'), max_length=255, blank=True, null=True)
	
	def __unicode__(self):
		return self.post.name
	
	class Meta:
		db_table            = 'crosspost'
		verbose_name        = _('Crosspost')
		verbose_name_plural = _('Crossposts')
