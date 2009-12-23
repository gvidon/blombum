# -*- mode: python; coding: utf-8; -*-

from time             import localtime, strftime
from os.path          import join, exists, isdir, getmtime

from django.template  import Library
from settingsDB.utils import SettingsCached

def gettime(filename):
    time = localtime(getmtime(filename))
    return strftime('%Y%m%d%H%M', time)

def theme_static(kind, filename):
    candidates = [[SettingsCached.param.THEME, kind, '%s.%s' % (filename, kind)],
                  [kind, '%s.%s' % (filename, kind)]]

    for candidate in candidates:
        full_path = join(SettingsCached.param.STATIC_ROOT, *candidate)
        if exists(full_path) and not isdir(full_path):
            url = '/'.join(candidate)
            if SettingsCached.param.APPEND_MTIME_TO_STATIC:
                url = '%s?%s' % (url, gettime(full_path))
            return {'STATIC_URL': SettingsCached.param.STATIC_URL, 'include': True, 'url': url}

    return {'include': False}

register = Library()

@register.inclusion_tag('templatetags/css.html')
def theme_css(filename='main'):
    return theme_static('css', filename)

@register.inclusion_tag('templatetags/js.html')
def theme_js(filename='main'):
    return theme_static('js', filename)

