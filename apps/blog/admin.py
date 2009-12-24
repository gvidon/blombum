# -*- mode: python; coding: utf-8; -*-

from django.contrib             import admin
from django.contrib.auth.models import User
from lib                        import libadmin
from blog.models                import Post
from settingsDB.utils           import SettingsCached       

class PostAdmin(libadmin.BFAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display        = ('name', 'date', 'author', 'enable_comments', 'comments_open', 'is_draft', 'site', 'view_link')
    search_fields       = ('name', 'text')
    list_filter         = ('date', 'is_draft', 'site')
    fieldsets           = (
        (None, {'fields': (('author', 'site'),
                           ('name', 'slug'),
                           'tags', 'text', 'render_method', 'date',
                           ('is_draft', 'enable_comments'))}),
        )

    class Media:
        if SettingsCached.param.WYSIWYG_ENABLE:
            js = (
                'http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js',
                
                '/tinymce/tiny_mce.js',
                #'/tinymce/jquery.tinymce.js',
                SettingsCached.param.STATIC_URL+'filebrowser/js/TinyMCEAdmin.js',
                #'/tinymce/init.js',
            )
            
            css = {'all': (
                SettingsCached.param.STATIC_URL+'js/tinymce/themes/simple/skins/default/ui.css',
                SettingsCached.param.STATIC_URL+'js/tinymce/themes/advanced/skins/default/ui.css',
                SettingsCached.param.STATIC_URL+'js/tinymce/themes/advanced/skins/o2k7/ui.css',
            )}
            
        elif SettingsCached.param.RENDER_METHOD in ('html', 'markdown', 'rst'):
            js = (SettingsCached.param.STATIC_URL + 'js/postimage.js', )

admin.site.register(Post, PostAdmin)
