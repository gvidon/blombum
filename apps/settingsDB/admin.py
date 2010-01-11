# -*- mode: python; coding: utf-8; -*-

from django.contrib    import admin
from settingsDB.models import Settings

class SettingsAdmin(admin.ModelAdmin):
	list_display        = ('name', 'is_enabled')
	list_filter         = ('name', 'is_enabled')
	search_fields       = ('name',)
	
	fieldsets           = ((None, {'fields': (
		('name', 'is_enabled'),
		('TAGLINE', 'FOOTER'),
		'ANONYMOUS_COMMENTS_APPROVED',
		('CAPTCHA', 'RECAPTCHA_PUBLIC_KEY', 'RECAPTCHA_PRIVATE_KEY', 'RECAPTCHA_THEME'),
		'GA_ACC_CODE',
		('FEEDBURNER_NAME', 'USE_ATOM', 'SHORT_POSTS_IN_FEED'),
		('LJ_USERNAME', 'LJ_PASSWORD'),
		'THEME'
	)}),)
	
admin.site.register(Settings, SettingsAdmin)
