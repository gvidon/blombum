from django.utils.translation import ugettext_lazy as _
from django.db                import models

#SIDE SERVICE DESCRIPTION WITH SPECIFIC USER DATA
class SideService(models.Model):
	name     = models.CharField(_(u'Account name'), max_length=128)
	url      = models.CharField(_(u'Your page URL'), max_length=128, blank=True)
	
	email    = models.CharField(_(u'Email'), max_length=128)
	login    = models.CharField(_(u'Login'), max_length=128, blank=True, null=True, help_text=_(u'Leave it empty if service uses email as login'))
	password = models.CharField(_(u'Password'), max_length=64)
	
	# required for blogger.com
	blogid   = models.CharField(_(u'Your blog id'), max_length=32, blank=True, null=True)
	
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
	code        = models.CharField(_(u'Security'), max_length=32, unique=True, blank=True, null=True)
	
	started_at  = models.DateTimeField(_(u'Process start time'), auto_now_add=True, blank=True, null=True)
	finished_at = models.DateTimeField(_(u'Process finish time'), blank=True, null=True)
	
	error_code  = models.CharField(_(u'Error code'), max_length=32, blank=True, null=True)
	error_stage = models.CharField(_(u'Error stage'), max_length=8, blank=True, null=True)
	
	url         = models.CharField(_(u'Crosspost URL'), max_length=255, blank=True, null=True)
	
	def __unicode__(self):
		return self.post.name
	
	class Meta:
		db_table            = 'crosspost'
		verbose_name        = _('Crosspost')
		verbose_name_plural = _('Crossposts')
