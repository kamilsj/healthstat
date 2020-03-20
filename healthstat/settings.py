import os
import sys
import django_heroku

#It has to be improved

try:
    from modules.secrets import AMAZON_DATA, DATABASE
except ImportError:
    exit('You have to edit secrets_default.py file and change its name to secrets.py.')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'drj#-%8h%k!&^e%@)8l1xn^_5546tm528^^zjp^pjlc_y=9o-_'
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'start',
    'api',
    'rest_framework',
    'django_heroku',
    'storages',
    'django_cron',
    'django_countries',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'healthstat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/html/'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'healthstat.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DATABASE[0],
        'USER': DATABASE[1],
        'PASSWORD': DATABASE[2],
        'HOST': DATABASE[3],
        'PORT': DATABASE[4],
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

django_heroku.settings(locals())

#S3
AWS_DEFAULT_ACL = 'public-read'
AWS_AUTO_CREATE_BUCKET = True
AWS_LOCATION = 'data'
AWS_ACCESS_KEY_ID = AMAZON_DATA[0]
AWS_SECRET_ACCESS_KEY =  AMAZON_DATA[1]
AWS_STORAGE_BUCKET_NAME = AMAZON_DATA[2]
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'html/static/'),
]
DEFAULT_FILE_STORAGE = 'healthstat.storage.MediaStorage'



AUTHENTICATION_BACKENDS = {
    'django.contrib.auth.backends.ModelBackend',
}

LOGIN_REDIRECT_URL = '/start/'
LOGOUT_REDIRECT_URL = '/'