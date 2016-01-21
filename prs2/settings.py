"""
Base Django settings for prs2 project.
Call and extend these settings by passing --settings=<PATH> to runserver, e.g.

> python manage.py runserver --settings=prs2.settings_dev.py
"""
from confy import database
import os
import sys
from unipath import Path

# Project paths
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).ancestor(2)
PROJECT_DIR = os.path.join(BASE_DIR, 'prs2')
# Add PROJECT_DIR to the system path.
sys.path.insert(0, PROJECT_DIR)

# Application definition
DEBUG = True if os.environ.get('DEBUG', False) else False
SECRET_KEY = os.environ['SECRET_KEY']
CSRF_COOKIE_SECURE = True if os.environ.get('CSRF_COOKIE_SECURE', False) == 'True' else False
SESSION_COOKIE_SECURE = True if os.environ.get('SESSION_COOKIE_SECURE', False) == 'True' else False
if not DEBUG:
    # Localhost, UAT and Production hosts:
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
        'prs.dpaw.wa.gov.au',
        'prs.dpaw.wa.gov.au.',
        'prs-uat.dpaw.wa.gov.au',
        'prs-uat.dpaw.wa.gov.au.',
    ]
INTERNAL_IPS = ['127.0.0.1', '::1']
ROOT_URLCONF = 'prs2.urls'
WSGI_APPLICATION = 'prs2.wsgi.application'
GEOSERVER_WMS_URL = os.environ.get('GEOSERVER_WMS_URL', '')
GEOSERVER_WFS_URL = os.environ.get('GEOSERVER_WFS_URL', '')
GEOCODER_URL = os.environ.get('GEOCODER_URL', '')
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'taggit',
    'reversion',
    'crispy_forms',
    'bootstrap_pagination',
    'tastypie',
    'explorer',  # django-sql-explorer
    'webtemplate_dpaw',
    'referral',
    'reports',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'dpaw_utils.middleware.SSOLoginMiddleware',
)
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.core.context_processors.request',
                'django.core.context_processors.csrf',
                'django.contrib.messages.context_processors.messages',
                'prs2.context_processors.template_context',
            ],
        },
    }
]
MANAGERS = (
    ('Sean Walsh', 'sean.walsh@dpaw.wa.gov.au', '9442 0306'),
    ('Cho Lamb', 'cho.lamb@dpaw.wa.gov.au', '9442 0309'),
)
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
APPLICATION_TITLE = 'Planning Referral System'
APPLICATION_ACRONYM = 'PRS'
APPLICATION_VERSION_NO = '2.0'
APPLICATION_ALERTS_EMAIL = 'PRS-Alerts@dpaw.wa.gov.au'
SITE_URL = os.environ['SITE_URL']
PRS_USER_GROUP = os.environ['PRS_USER_GROUP']
PRS_POWER_USER_GROUP = os.environ['PRS_PWUSER_GROUP']
ALLOWED_UPLOAD_TYPES = [
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.ms-word.document.12',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/xml',
    'application/pdf',
    'application/zip',
    'application/x-zip',
    'application/x-zip-compressed',
    'application/octet-stream',  # MIME type for zip files in Chrome.
    'application/vnd.ms-outlook',  # Outlook MSG format.
    'image/tiff',
    'image/jpeg',
    'image/gif',
    'image/png',
    'text/csv',
    'text/html',
    'text/plain'
]

# Email settings
ADMINS = ('asi@dpaw.wa.gov.au',)
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']

# Database configuration
DATABASES = {
    # Defined in the DATABASE_URL env variable.
    'default': database.config(),
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Australia/Perth'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Sensible AU date input formats
DATE_INPUT_FORMATS = (
    '%d/%m/%Y',
    '%d/%m/%y',
    '%d-%m-%Y',
    '%d-%m-%y',
    '%d %b %Y',
    '%d %b, %Y',
    '%d %B %Y',
    '%d %B, %Y',
    '%Y-%m-%d'  # Needed for form validation.
)

# Static files (CSS, JavaScript, Images)
# Ensure that the media directory exists:
if not os.path.exists(os.path.join(BASE_DIR, 'media')):
    os.mkdir(os.path.join(BASE_DIR, 'media'))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'prs2', 'static'),)

# This is required to add context variables to all templates:
STATIC_CONTEXT_VARS = {}

# Logging settings
# Ensure that the logs directory exists:
if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.mkdir(os.path.join(BASE_DIR, 'logs'))
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'prs.log'),
            'formatter': 'verbose',
            'maxBytes': '16777216'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'INFO'
        },
        'log': {
            'handlers': ['file'],
            'level': 'INFO'
        },
    }
}
DEBUG_LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'debug-prs.log'),
            'formatter': 'verbose',
            'maxBytes': '16777216'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG'
        },
        'log': {
            'handlers': ['file'],
            'level': 'DEBUG'
        },
    }
}


# Supplement some settings when DEBUG is True.
if DEBUG:
    LOGGING = DEBUG_LOGGING
    if os.environ.get('INTERNAL_IP', False):  # Optionally add developer local IP
        INTERNAL_IPS.append(os.environ['INTERNAL_IP'])
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    DEBUG_TOOLBAR_PATCH_SETTINGS = True
    MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE_CLASSES

# Tastypie settings
TASTYPIE_DEFAULT_FORMATS = ['json']

# crispy_forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# django-sql-explorer settings
EXPLORER_PERMISSION_VIEW = lambda u: u.is_staff and u.userprofile.is_power_user()
