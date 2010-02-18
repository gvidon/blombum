# -*- mode: python; coding: utf-8; -*-
from django.contrib.auth.models import User
from django.contrib             import admin

from crossposting.admin         import BFPostAdmin
from settingsDB.utils           import SettingsCached
from blog.models                import Post
from lib                        import libadmin

class PostAdmin(BFPostAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display        = ('name', 'date', 'author', 'enable_comments', 'comments_open', 'is_draft', 'site', 'view_link')
    search_fields       = ('name', 'text')
    list_filter         = ('date', 'is_draft', 'site')
    fieldsets           = (
        (None, {'fields': (('author', 'site'),
                           ('name', 'slug'),
                           ('crossposting_que',),
                           'tags', 'text', 'render_method', 'date',
                           ('is_draft', 'enable_comments'))}),
        )

    class Media:
        if SettingsCached.param.WYSIWYG_ENABLE:
            js = (
                'http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js',
                
                '/tinymce/tiny_mce.js',
                SettingsCached.param.STATIC_URL+'filebrowser/js/TinyMCEAdmin.js',
                
                SettingsCached.param.STATIC_URL+'js/jqModal.js',
                SettingsCached.param.STATIC_URL+'js/crossposting.js',
            )
            
            css = {'all': (
                SettingsCached.param.STATIC_URL+'css/jqModal.css',
                SettingsCached.param.STATIC_URL+'css/crossposting.css',
                
                SettingsCached.param.STATIC_URL+'js/tinymce/themes/simple/skins/default/ui.css',
                SettingsCached.param.STATIC_URL+'js/tinymce/themes/advanced/skins/default/ui.css',
                SettingsCached.param.STATIC_URL+'js/tinymce/themes/advanced/skins/o2k7/ui.css',
            )}
            
        elif SettingsCached.param.RENDER_METHOD in ('html', 'markdown', 'rst'):
            js = (SettingsCached.param.STATIC_URL + 'js/postimage.js', )

admin.site.register(Post, PostAdmin)
