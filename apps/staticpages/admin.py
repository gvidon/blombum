# -*- mode: python; coding: utf-8; -*-

from django.contrib import admin
from models         import StaticPage

class StaticPageAdmin(admin.ModelAdmin):
	list_display = ('title', 'url')
	
admin.site.register(StaticPage, StaticPageAdmin)
