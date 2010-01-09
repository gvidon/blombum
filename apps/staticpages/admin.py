# -*- mode: python; coding: utf-8; -*-

from django.contrib import admin
from models         import StaticPage
from forms          import StaticPageAdminForm

class StaticPageAdmin(admin.ModelAdmin):
	list_display = ('title', 'url')
	form         = StaticPageAdminForm
	
admin.site.register(StaticPage, StaticPageAdmin)
