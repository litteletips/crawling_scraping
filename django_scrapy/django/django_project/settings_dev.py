"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 2.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import os.path
CONF_ROOT = os.path.dirname(__file__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-3v0!-0hh9^q&z)j9gsn+7@_-3*-u0w#c)qcw66otp1eoj*c0j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',

    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',

    ###'allauth.socialaccount.providers.facebook',

    #'snippets',
    #'registration',
    'after_response',
    'bootstrapform',
    'ws4redis',
    #'chatserver',
    #'tornado_websockets',
    
    #'users',
    #'custom_user',
    
    #'django_mongoengine',
    #'nutrition',

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

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'osaki1choume',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "/opt/static"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
#    '/var/www/main/cgi-bin/mysite/static/',
#    ("static", "/static"),
]


# Django Registration Settings.
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
EMAIL_USE_TLS = False
#EMAIL_USE_SSL = True
#EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
#MAILER_EMAIL_BACKEND = EMAIL_BACKEND

#EMAIL_HOST = 'localhost'
EMAIL_HOST = 'mymailserver'
#EMAIL_HOST  = os.environ.get('MYMMAILSERVER_PORT_25_TCP_ADDR', '')
#EMAIL_PORT = 25
EMAIL_PORT  = os.environ.get('MYMMAILSERVER_PORT_25_TCP_PORT', '')
#REGISTRATION_TEMPLATE_DIR = os.path.join(BASE_DIR, "allauth_templates", "mytemplates")

#EMAIL_HOST = 'smtp.gmail.com'                                                                                                                                           
#EMAIL_PORT = 465
#EMAIL_USE_TLS = True
#EMAIL_HOST_USER = 'myemail@gmail.com'
#EMAIL_HOST_PASSWORD = 'mypassword'
#DEFAULT_FROM_EMAIL = 'myemail@gmail.com'




#WSGI_APPLICATION = 'mysite.wsgi.application'
LOGIN_URL='/account/login/'

#LOGIN_REDIRECT_URL = '/account/login/'

LOGIN_REDIRECT_URL = '/'

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
APPEND_SLASH=True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.request",

    'django.core.context_processors.static',
    'ws4redis.context_processors.default',

    # Disabling due to alluth>=0.21.0 changes
    # "allauth.account.context_processors.account",
    # "allauth.socialaccount.context_processors.socialaccount",
)

WSGI_APPLICATION = 'mysite.wsgi.application'

REST_SESSION_LOGIN = False
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

    # Kerberos
    #'django.contrib.auth.backends.RemoteUserBackend',

    #'mysite.auth_backends.CustomUserModelBackend',

    #'mongoengine.django.auth.MongoEngineBackend',
)

SITE_ID = 1
#ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
#ACCOUNT_AUTHENTICATION_METHOD = 'email'
#ACCOUNT_AUTHENTICATION_METHOD = 'username'
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
#ACCOUNT_EMAIL_VERIFICATION = 'optional'

ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

#ACCOUNT_ADAPTER = 'mining.views.MyAccountAdapter'

#ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'

# For Custom User Model
#ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

#AUTH_USER_MODEL = 'mining.CustomUser'
#AUTH_USER_MODEL = 'custom_user.EmailUser'

###AUTH_USER_MODEL = 'users.AuthUser'
###AUTH_USER_MODEL = 'nutrition.MyCustomEmailUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        #'rest_framework.permissions.IsAdminUser',
        #'rest_framework.permissions.AllowAny',
    ),
    'PAGE_SIZE': 10, 
}


CACHE_BACKEND = 'dummy://'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


WEBSOCKET_URL = '/ws/'

WS4REDIS_CONNECTION = {
    'host': os.environ.get('MYREDIS_PORT_6379_TCP_ADDR', ''),
    'port': os.environ.get('MYREDIS_PORT_6379_TCP_PORT', ''),
    'db': 0,
    #'password': 'verysecret',
}

WS4REDIS_EXPIRE = 7200
WS4REDIS_PREFIX = 'ws'
#WS4REDIS_HEARTBEAT = '--heartbeat--'
#WS4REDIS_HEARTBEAT = '{"hb","-hb-"}'
WS4REDIS_HEARTBEAT = '{"type":"pong","user":"system","message":"--heartbeat--"}'
#WS4REDIS_SUBSCRIBER = 'myapp.redis_store.RedisSubscriber'
#WSGI_APPLICATION = 'ws4redis.django_runserver.application'

#SESSION_ENGINE = 'redis_sessions.session'
#SESSION_REDIS_PREFIX = 'session'
"""
import tornado_websockets
import tornado.web
TORNADO = {
    'port': 3031,    # 8000 by default
    'handlers': [
        # ...
        tornado_websockets.django_app, 
        #(r'%s(.*)' % STATIC_URL, tornado.web.StaticFileHandler, {'path': STATIC_ROOT}),
        # django_app is using a "wildcard" route, so it should be the last element
    ],
    'settings': {
        'debug': True,
    }

}
"""

#SESSION_ENGINE = 'django_mongoengine.sessions'
#SESSION_SERIALIZER = 'django_mongoengine.sessions.BSONSerializer'


# ロギング設定
LOGGING = {
    'version': 1,  # 1固定
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}
