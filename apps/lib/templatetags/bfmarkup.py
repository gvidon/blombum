# -*- mode: python; coding: utf-8; -*-

"""
Byteflow's own markup filters to avoid using of django's currently broken
as of 12.02.2008.
For status see http://code.djangoproject.com/ticket/6387
"""

from django import template
from django.conf import settings
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def strong_spaces(value):
    '''
    Replace spaces with non-breaking space html entities.
    '''
    return mark_safe(value.replace(u' ',u'&nbsp;'))
strong_spaces.is_safe = True


@register.filter
def markdown(value, arg=''):
    """
    Runs Markdown over a given value, optionally using various
    extensions python-markdown2 supports.

    Syntax::

        {{ value|markdown:"extension1_name,extension2_name..." }}

    To enable safe mode, which strips raw HTML and only returns HTML
    generated by actual Markdown syntax, pass "safe" as the first
    extension in the list.

    If the version of Markdown in use does not support extensions,
    they will be silently ignored.

    """
    try:
        import markdown2
    except ImportError:
        if settings.DEBUG:
            raise template.TemplateSyntaxError, "Error in {% markdown %} filter: The Python markdown2 library isn't installed."
        return force_unicode(value)
    else:
       	extensions = [e for e in arg.split(",") if e]
        if len(extensions) > 0 and extensions[0] == "safe":
            extensions = extensions[1:]
            safe_mode = True
        else:
            safe_mode = False
        return mark_safe(markdown2.markdown(force_unicode(value), extras=extensions, safe_mode=safe_mode))
markdown.is_safe = True


@register.filter
def cond_display(value, variants):
    '''
    Truth of value is used to determine which of variants to display.

    Variants are two strings, separated by comma. First is displayed in case
    value is False, otherwise second is displayed.
    '''
    return mark_safe(variants.split(',')[bool(value)])


@register.filter
def list_attr(value, attr_name):
    '''
    Given a list of objects will try to retrieve attribute from each of them,
    calling it if it's callable
    '''
    def get_attr(item):
        attr = getattr(item, attr_name, None)
        if callable(attr):
            return attr()
        return attr
    return [get_attr(item) for item in value]


@register.filter
def get_key(dictionary, key):
    '''
    Returns value from dictionary, identified by key. If there is no such key in
    dictionary, returns empty string.

    Useful when your key is variable.
    '''
    try:
        return dictionary[key]
    except KeyError:
        return ''
    except TypeError:
        raise template.TemplateSyntaxError(
            u"Supplied argument is not a dictionary: %s" %
            unicode(dictionary)[:10])


@register.filter
@stringfilter
def startswith(value, arg):
    '''
    Check if value starts with argument.
    '''
    try:
        arg = str(arg)
    except (ValueError, TypeError):
        return value
    return value.startswith(arg)
startswith.is_safe = True


@register.filter
def dayssince(dt1, dt2):
    """
    Number of days between dt1 and dt2.

    Counts difference between days as numbers and not as 24-hour cycles.
    """
    return (dt1.date() - dt2.date()).days


@register.inclusion_tag('templatetags/relative_datetime.html')
def relative_datetime(orig, new):
    time = new.strftime("%H:%M")
    if orig.date() != new.date():
        days = dayssince(new, orig)
    else:
        days = None
    return {'time': time, 'days': days}
