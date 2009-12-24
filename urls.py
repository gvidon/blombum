# Custom patches
import patches
from os.path                   import join, dirname

from django.conf               import settings
from django.conf.urls.defaults import *
from django.contrib            import admin
from django.contrib.sitemaps   import FlatPageSitemap, GenericSitemap
from django.http               import HttpResponseServerError
from django.template.context   import RequestContext, Context
from django.template.loader    import render_to_string

from blog.sitemaps             import BlogSitemap, IndexSitemap, BlogTagsSitemap
from tagging.models            import Tag
from lib                       import appcheck

def error500(request, template_name='500.html'):
    try:
        output = render_to_string(template_name, {}, RequestContext(request))
    except:
        output = "Critical error. Administrator was notified."
    return HttpResponseServerError(output)

handler500 = 'urls.error500'

sitemaps = {
    'blog'    : BlogSitemap,
    'blogtags': BlogTagsSitemap,
    'flat'    : FlatPageSitemap,
    'index'   : IndexSitemap,
}

try:
    import urls_local
    urlpatterns = urls_local.urlpatterns
except ImportError:
    urlpatterns = patterns('',)

admin.autodiscover()

urlpatterns += patterns(
    '',
    url(r''                                , include('revcanonical.urls')),
    url(r'^admin/postimage/'               , include('postimage.urls')),
    url(r'^admin/filebrowser/'             , include('filebrowser.urls')),
    
    url(r'^admin/(.*)'                     , admin.site.root, name='admin'),
    
    url(r'^accounts/'                      , include('accounts.urls')),
    url(r'^openid/'                        , include('openidconsumer.urls')),
    url(r'^openidserver/'                  , include('openidserver.urls')),
    url(r'^%s' % settings.BLOG_URLCONF_ROOT, include('blog.urls')),
    url(r'^sitemap.xml$'                   , 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^xmlrpc/'                        , include('xmlrpc.urls')),
    url(r'^captcha/'                       , include('captcha.urls')),
    url(r'^robots.txt$'                    , include('robots.urls')),
    url(r'^feeds/'                         , include('feed.urls')),
    
    # tinymce and admin page for blog post must on the same domain
    url(r'^tinymce/'                       , include('tinymce.urls')),
)

if appcheck.watchlist:
    urlpatterns += patterns('', url(r'^watchlist/', include('watchlist.urls')),)

if appcheck.friends:
    urlpatterns += patterns('', url(r'^friends/', include('friends.urls')),)

if settings.URL_ROOT_HANDLER:
    urlpatterns += patterns('', url(r'^$', settings.URL_ROOT_HANDLER))

if appcheck.wpimport:
    urlpatterns += patterns('', url(r'^wpimport/', include('wpimport.urls')),)

if appcheck.debug:
    urlpatterns += patterns('', url('', include('debug.urls')),)

if appcheck.life:
    urlpatterns += patterns('', url(r'^life/', include('life.urls')),)

# static pages URLs
urlpatterns += patterns('', url(r'^/?', include('staticpages.urls')),)
