import os
from pathlib import Path
from datetime import timedelta
from decouple import config, Csv
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-this-now')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', 
    default='.onrender.com,localhost,127.0.0.1,.serialco.tv,www.serialco.tv,.cloudshell.dev,.vercel.app',
    cast=Csv()
)

CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS',
    default='https://*.cloudshell.dev,https://*.serialco.tv,https://*.onrender.com,https://*.vercel.app',
    cast=Csv()
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',  
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'cloudinary',  
    'rest_framework',
    'corsheaders',
    'accounts',
    'content',
    'serials',
    'store',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'serialcotv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'serialcotv.wsgi.application'

# استخدام Supabase Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('SUPABASE_DB_NAME', default='postgres'),
        'USER': config('SUPABASE_DB_USER', default='postgres'),
        'PASSWORD': config('SUPABASE_DB_PASSWORD', default=''),
        'HOST': config('SUPABASE_DB_HOST', default='db.supabase.co'),
        'PORT': config('SUPABASE_DB_PORT', default='5432'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STORAGES = {
    "default": {"BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME', default='rsmjekym'),
    'API_KEY': config('CLOUDINARY_API_KEY', default=''),
    'API_SECRET': config('CLOUDINARY_API_SECRET', default=''),
}

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['authorization', 'content-type', 'x-requested-with', 'accept', 'origin', 'x-csrftoken']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'accounts.authentication.CustomerJWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '1000/hour'
    }
}

JWT_SECRET_KEY = config('JWT_SECRET_KEY', default=SECRET_KEY)
JWT_ALGORITHM = 'HS256'
WALLET_CHARGE_SECRET = config('WALLET_CHARGE_SECRET', default='wallet-secret-key-123')

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CHARGILY_SECRET_KEY = config('CHARGILY_SECRET_KEY', default='')
CHARGILY_PUBLIC_KEY = config('CHARGILY_PUBLIC_KEY', default='')
CHARGILY_APP_SECRET = config('CHARGILY_APP_SECRET', default='')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'verbose': {'format': '[{levelname}] {asctime} {module} {message}', 'style': '{'}},
    'handlers': {'console': {'class': 'logging.StreamHandler', 'formatter': 'verbose'}},
    'root': {'handlers': ['console'], 'level': 'INFO'},
    'loggers': {
        'django': {'handlers': ['console'], 'level': 'INFO', 'propagate': False},
        'serials': {'handlers': ['console'], 'level': 'INFO', 'propagate': False},
    },
}