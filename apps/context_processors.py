import os.path

from django.views.debug          import get_safe_settings
from django.contrib.sites.models import Site
from blog.models                 import Post

from lib                         import appcheck
from settingsDB.utils            import SettingsCached

class SafeSettings:
    def __init__(self):
        self._settings = None
    
    def __getattr__(self, name):
        # Lazy load of settings.
        if self._settings is None:
            self._settings = get_safe_settings()
        # get_safe_settings only returns upper case settings, so let's not worry
        # about case sensitivity.
        name = name.upper()
        try:
            return self._settings[name]
        except KeyError:
            # This method should return the (computed) attribute value or raise 
            # an AttributeError exception.
            raise AttributeError

settings = SafeSettings()

def settings_vars(request):
    return {
        'STATIC_URL'      : SettingsCached.param.STATIC_URL,
        'THEME_STATIC_URL': SettingsCached.param.THEME_STATIC_URL,
        'settings'        : SettingsCached.param,
        'appcheck'        : appcheck,
        'site'            : Site.objects.get_current(),
    }
