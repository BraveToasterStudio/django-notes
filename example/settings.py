import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG
ADMINS = ()
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, '../django_notes.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, "../static"))
STATIC_URL = "/static/"
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
SECRET_KEY = '#!nz=0@+8a2k!vorz5%q6kp6)it#o5jhtrtg*%=07u)(5x6(fb'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_URLCONF = 'example.urls'
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',

    'staticfiles',
    'tinymce',
    'django_nose',

    'django_notes',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

TINYMCE_JS_URL = os.path.join(STATIC_URL, "tiny_mce/tiny_mce.js")
TINYMCE_DEFAULT_CONFIG = {'theme': "advanced", 'relative_urls': False}
FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, "fixtures"),
)
