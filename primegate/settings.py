"""
Django settings for primegate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from config import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
gettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kvw2shpgw$5=kvza&q0pin%2s)=_c*bh(f=2u4yjo2r5n0#39h'

# SECURITY WARNING: don't run with debug turned on in production!
if PRODUCTION == False:
    DEBUG = True
else:
    DEBUG = False

TEMPLATE_DEBUG = True
if DEBUG == True:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['.primegateacademy.com']
    #ROOT_URLCONF = 'primegate.urls'
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_WHITELIST = ('http://www.primegateacademy.com','http://primegateacademy.com','http://localhost')
    #CORS_ORIGIN_REGEX_WHITELIST = ('^(https?://)?(\w+\.)?primegateacademy\.com$', )

    


# Application definition

INSTALLED_APPS = (
    'grappelli',   
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'publicpages',
    'south',
    'nlsubscribers'
    #'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'primegate.urls'

WSGI_APPLICATION = 'primegate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': DBNAME,
       
        'USER': DBUSER,                      # Not used with sqlite3.
        'PASSWORD':DBPASS,                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        #'PORT': '5332',                      # Set to empty string for default. Not used wit
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
if DEBUG == True:
    STATIC_ROOT = os.path.join(PROJECT_PATH, "static")
    STATIC_URL = '/static/'
else:
    STATIC_ROOT = PRODUCTION_STATIC_ROOT
    STATIC_URL = PRODUCTION_STATIC_URL

MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"


#print "Project Path:" + PROJECT_PATH
#print "Base Dir:"+ BASE_DIR
#print "STATIC ROOT  Path:"+ STATIC_ROOT
#print "STATIC URL:" +STATIC_URL
#print "MEDIA Root:" + MEDIA_ROOT
#print "Media URL:" + MEDIA_URL
#print  (os.path.dirname(__file__))
STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__),"static"),)
#for st in STATICFILES_DIRS:
    #print str(STATICFILES_DIRS)
    
EMAIL_HOST = EMAIL_HOST
EMAIL_PORT = EMAIL_PORT
EMAIL_HOST_USER =  EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = True
#EMAIL_USE_SSL
INTERNAL_IPS =  ('127.0.0.1',)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates"),
)
