# -*- mode: python; coding: utf-8; -*-

from discussion.models import CommentNode
from django.contrib    import admin

class CommentNodeAdmin(admin.ModelAdmin):
    list_display = ('get_clean_html', 'user', 'pub_date', 'content_type',
                    'object_id', 'reply_to_id', 'approved')
    list_filter = ('approved',)
    actions = ['comment_approve']

    def comment_approve(self, request, queryset):
        count = queryset.update(approved=True)
        msg = (count == 1) and 'One comment was' or ('%s comments were' % count)
        self.message_user(request, "%s approved." % msg)
    comment_approve.short_description = 'Mark selected comments as approved'

admin.site.register(CommentNode, CommentNodeAdmin)
