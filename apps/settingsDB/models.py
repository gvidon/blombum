from django.db import models

#MODEL FOR STORING SETTINGS.PY PARAMS
class Settings(models.Model):
	name                        = models.CharField(verbose_name='Configuration set name', max_length='128')
	is_enabled                  = models.BooleanField(verbose_name='Enable this config', blank=True, default=False)
	
	TAGLINE                     = models.CharField(verbose_name='Tag line', max_length='255', blank=True, default='')
	FOOTER                      = models.CharField(verbose_name='Footer sign', max_length='255', blank=True, default='')
	
	ANONYMOUS_COMMENTS_APPROVED = models.BooleanField(verbose_name='Allow anonymous comments', blank=True, default=False)
	
	# process it separately in hash (settings_local.py)
	RECAPTCHA_PUBLIC_KEY        = models.CharField(verbose_name='Recaptcha public key', max_length=128, blank=True, default='')
	RECAPTCHA_PRIVATE_KEY       = models.CharField(verbose_name='Recaptcha private key', max_length=128, blank=True, default='')
	
	# process it separately in hash (settings_local.py)
	GA_ACC_CODE                 = models.CharField(verbose_name='GoogleAnalytics code', max_length=255, blank=True, default='')
	
	# process it separately in hash (settings_local.py)
	FEEDBURNER_NAME             = models.CharField(verbose_name='Your feed name in feedburner', max_length=128, blank=True, default='')
	USE_ATOM                    = models.BooleanField(verbose_name='Use ATOM instead of RSS', blank=True, default=True)
	SHORT_POSTS_IN_FEED         = models.BooleanField(verbose_name='Full or short posts in feed', blank=True, default=True)
	
	LJ_USERNAME                 = models.CharField(verbose_name='LJ account username', max_length=64, blank=True, default='')
	LJ_PASSWORD                 = models.CharField(verbose_name='LJ account password', max_length=64, blank=True, default='')
	
	PAGINATE_BY                 = models.IntegerField(verbose_name='Blog entries per page', blank=True, default=10)
	
	BLOG_URLCONF_ROOT           = models.CharField(verbose_name='Blog path. Don\'t forget that there must be no leading \'/\'', max_length=64, blank='True', default='blog/')
	THEME                       = models.CharField(verbose_name='Blog templates theme', max_length=64, blank=True, default='orange')
	
	CAPTCHA = models.CharField(verbose_name='Captcha type', choices=(
		(''         , 'None'),
		('simple'   , 'Simple'),
		('recaptcha', 'Recaptcha'),
	), max_length='9', blank=True, default='')
