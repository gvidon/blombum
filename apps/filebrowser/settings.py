# coding: utf-8

# imports
import os

# django imports
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# settings for django-tinymce
try:
    import tinymce.settings
    DEFAULT_URL_TINYMCE  = tinymce.settings.JS_BASE_URL + '/'
    DEFAULT_PATH_TINYMCE = tinymce.settings.JS_ROOT + '/'
except ImportError:
    DEFAULT_URL_TINYMCE  = settings.STATIC_URL + "js/tinymce/"
    DEFAULT_PATH_TINYMCE = os.path.join(settings.STATIC_ROOT, 'js/tinymce/')

DEBUG                    = False

MEDIA_ROOT               = settings.MEDIA_ROOT
MEDIA_URL                = settings.MEDIA_URL

# Main FileBrowser Directory. This has to be a directory within MEDIA_ROOT.
# Leave empty in order to browse all files under MEDIA_ROOT.
# DO NOT USE A SLASH AT THE BEGINNING, DO NOT FORGET THE TRAILING SLASH AT THE END.
DIRECTORY               = settings.MEDIA_ROOT+'/'

URL_FILEBROWSER_MEDIA   = os.path.join(settings.STATIC_URL, 'filebrowser/')
PATH_FILEBROWSER_MEDIA  = os.path.join(settings.STATIC_ROOT, 'filebrowser/')

URL_TINYMCE             = DEFAULT_URL_TINYMCE
PATH_TINYMCE            = DEFAULT_PATH_TINYMCE

# Directory to Save Image Versions (and Thumbnails). Relative to MEDIA_ROOT.
# If no directory is given, versions are stored within the Image directory.
# VERSION URL: VERSIONS_BASEDIR/original_path/originalfilename_versionsuffix.extension
VERSIONS_BASEDIR        = ''

ADMIN_VERSIONS          = ['thumbnail','small', 'medium','big']
ADMIN_THUMBNAIL         = 'fb_thumb'

# EXTRA SETTINGS
# True to save the URL including MEDIA_URL to your model fields
# or False (default) to save path relative to MEDIA_URL.
# Note: Full URL does not necessarily means absolute URL.
SAVE_FULL_URL           = True
STRICT_PIL              = False

# PIL's Error "Suspension not allowed here" work around:
# s. http://mail.python.org/pipermail/image-sig/1999-August/000816.html
IMAGE_MAXBLOCK          = 1024*1024


MAX_UPLOAD_SIZE         = 10485760

# Convert Filename (replace spaces and convert to lowercase)
CONVERT_FILENAME        = True

LIST_PER_PAGE           = 50

DEFAULT_SORTING_BY      = 'date'
DEFAULT_SORTING_ORDER   = 'desc'

# Allowed Extensions for File Upload. Lower case is important.
# Please be aware that there are Icons for the default extension settings.
# Therefore, if you add a category (e.g. "Misc"), you won't get an icon.
EXTENSIONS = {
    'Folder'  : [''],
    'Image'   : ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Video'   : ['.mov','.wmv','.mpeg','.mpg','.avi','.rm'],
    'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
    'Audio'   : ['.mp3','.mp4','.wav','.aiff','.midi','.m4p'],
    'Code'    : ['.html','.py','.js','.css']
}

# Exclude files matching any of the following regular expressions
# Default is to exclude 'thumbnail' style naming of image-thumbnails.
EXTENSION_LIST          = []
for exts in EXTENSIONS.values(): EXTENSION_LIST += exts

EXCLUDE                 = (r'_(%(exts)s)_.*_q\d{1,3}\.(%(exts)s)' % {'exts': ('|'.join(EXTENSION_LIST))},)

# Define different formats for allowed selections.
# This has to be a subset of EXTENSIONS.
SELECT_FORMATS = {
    'File'    : ['Folder','Document',],
    'Image'   : ['Image'],
    'Media'   : ['Video','Sound'],
    'Document': ['Document'],
    
    # for TinyMCE we can also define lower-case items
    'image'   : ['Image'],
    'file'    : ['Folder','Image','Document',],
}

# Versions Format. Available Attributes: verbose_name, width, height, opts
VERSIONS = {
    'fb_thumb'        : {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop upscale'},
    'thumbnail'       : {'verbose_name': 'Thumbnail (140px)', 'width': 140, 'height': '', 'opts': ''},
    'small'           : {'verbose_name': 'Small (300px)', 'width': 300, 'height': '', 'opts': ''},
    'medium'          : {'verbose_name': 'Medium (460px)', 'width': 460, 'height': '', 'opts': ''},
    'big'             : {'verbose_name': 'Big (620px)', 'width': 620, 'height': '', 'opts': ''},
    'cropped'         : {'verbose_name': 'Cropped (60x60px)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'croppedthumbnail': {'verbose_name': 'Cropped Thumbnail (140x140px)', 'width': 140, 'height': 140, 'opts': 'crop'},
}

# EXTRA TRANSLATION STRINGS
# The following strings are not availabe within views or templates
_('Folder')
_('Image')
_('Video')
_('Document')
_('Audio')
_('Code')


