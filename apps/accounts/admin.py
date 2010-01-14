# -*- mode: python; coding: utf-8; -*-
from django.contrib.sites.models import Site
from django.contrib.sites.admin  import SiteAdmin
from django.contrib.auth.admin   import UserAdmin
from django.contrib              import admin

from accounts.models             import ActionRecord
from accounts.forms              import BfUserChangeForm

UserAdmin.form = BfUserChangeForm

UserAdmin.fieldsets += (
    ('Byteflow Extensions', {'fields': ('site', 'email_new')}),
)

UserAdmin.list_display  = ('username', 'email', 'first_name', 'is_staff', 'is_active')
UserAdmin.search_fields = ('username', 'first_name', 'email')

class ActionRecordAdmin(admin.ModelAdmin):
    list_display  = ('user', 'date')
    search_fields = ['user']
    list_filter   = ('user', 'date')

#admin.site.register(ActionRecord, ActionRecordAdmin)
admin.site.unregister(Site)
