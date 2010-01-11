# This code is public domain.
# Thanks to SmileyChris for the original implementation

import librecaptcha

from django.contrib.sites.models import Site
from django.utils.translation    import ugettext_lazy as _
from django.utils.safestring     import mark_safe
from django                      import forms

from settingsDB.utils            import SettingsCached

# Do you want to bypass reCAPTCHA validation while in DEBUG mode?
SKIP_IF_IN_DEBUG_MODE = False

### ERROR_CODES
ERROR_CODES = {
    "unknown" :	_("Unknown error."),
    "invalid-site-public-key" :	_("We weren't able to verify the public key. Please try again later."),
    "invalid-site-private-key" : _("We weren't able to verify the private key. Please try again later."),
    "invalid-request-cookie" : _("The challenge parameter of the verify script was incorrect."),
    "incorrect-captcha-sol" : _("The CAPTCHA solution was incorrect."),
    "verify-params-incorrect" : _("The parameters to /verify were incorrect, make sure you are passing all the required parameters.  Please try again later."),
    "invalid-referrer" : _("reCAPTCHA API keys are tied to a specific domain name for security reasons.  Please try again later."),
    "recaptcha-not-reachable" :	_("Unable to contact the reCAPTCHA verify server.  Please try again later.")
}


class RecaptchaWidget(forms.Widget):
    def __init__(self):
       super(RecaptchaWidget, self).__init__()

    def render(self, name, value, attrs=None):
        try:
            pubkey = SettingsCached.param.RECAPTCHA_PUBLIC_KEY
        #FIXED 23.13.2009
        #except IndexError:
        except (IndexError, KeyError):
            return mark_safe(u'<p>Recaptcha is not configured properly.</p>')
        html = librecaptcha.displayhtml(pubkey,
                                        theme=SettingsCached.param.RECAPTCHA_THEME,
                                        lang=SettingsCached.param.LANGUAGE_CODE[:2])
        return mark_safe(html)

    def value_from_datadict(self, data, files, name):
        challenge = data.get('recaptcha_challenge_field')
        response = data.get('recaptcha_response_field')
        return (challenge, response)

    def id_for_label(self, id_):
        return None


class RecaptchaField(forms.Field):
    widget = RecaptchaWidget

    def __init__(self, remote_ip, *args, **kwargs):
        self.remote_ip = remote_ip
        super(RecaptchaField, self).__init__(*args, **kwargs)

    def clean(self, value):
        if SKIP_IF_IN_DEBUG_MODE and SettingsCached.param.DEBUG:
            return True
        value = super(RecaptchaField, self).clean(value)
        challenge, response = value

        if not challenge:
            raise forms.ValidationError(_('An error occured with the CAPTCHA service. Please try again.'))
        if not response:
            raise forms.ValidationError(_('Please enter the CAPTCHA solution.'))

        try:
            privkey = SettingsCached.param.RECAPTCHA_PRIVATE_KEY
        except IndexError:
            # In case of reCaptcha misconfiguration we think that comment is good
            return True
        rc = librecaptcha.submit(challenge, response, privkey, self.remote_ip)
        if not rc.is_valid:
            msg = ERROR_CODES.get(rc.error_code, ERROR_CODES['unknown'])
            raise forms.ValidationError(msg)

        # reCAPTCHA validates!
        return True

