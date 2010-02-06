# -*- mode: python; coding: utf-8; -*-
from django.contrib      import admin
from crossposting.models import Crosspost, SideService

class SideServiceAdmin(admin.ModelAdmin):
	list_display        = ('name', 'url', 'login', 'type')
	search_fields       = ('name', 'url', 'login', 'type')
	list_filter         = ('name', 'url', 'login', 'type')

class CrosspostAdmin(admin.ModelAdmin):
	list_display = ('post', 'service')

admin.site.register(Crosspost, CrosspostAdmin)
admin.site.register(SideService, SideServiceAdmin)
