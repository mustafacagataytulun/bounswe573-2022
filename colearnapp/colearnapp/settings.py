"""
Django settings for colearnapp project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except KeyError:
    print('SECRET_KEY environment variable must be defined for Django to work.')
    sys.exit(1)

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.environ.get('DEBUG') if os.environ.get('DEBUG') else False

ALLOWED_HOSTS = [
    'colearnapp.mustafatulun.com',
    'colearnapp-7r3xxs4pca-ew.a.run.app',
    'localhost',
]

SECURE_HSTS_SECONDS  = os.environ.get('SECURE_HSTS_SECONDS') if os.environ.get('SECURE_HSTS_SECONDS') else 0
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = os.environ.get('IS_HTTPS_ENABLED') if os.environ.get('IS_HTTPS_ENABLED') else False
CSRF_COOKIE_SECURE = os.environ.get('IS_HTTPS_ENABLED') if os.environ.get('IS_HTTPS_ENABLED') else False
CSRF_TRUSTED_ORIGINS = [
    'https://colearnapp.mustafatulun.com',
    'https://colearnapp-7r3xxs4pca-ew.a.run.app',
]

# Application definition

INSTALLED_APPS = [
    'users',
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

ROOT_URLCONF = 'colearnapp.urls'

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

WSGI_APPLICATION = 'colearnapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DB_NAME = os.environ.get('DB_NAME') if os.environ.get('DB_NAME') else 'colearnapp'
DB_USER = os.environ.get('DB_USER') if os.environ.get('DB_USER') else 'postgres'
DB_HOST = os.environ.get('DB_HOST') if os.environ.get('DB_HOST') else 'localhost'
DB_PORT = os.environ.get('DB_PORT') if os.environ.get('DB_PORT') else 5432

try:
    DB_PASSWORD = os.environ['DB_PASSWORD']
except KeyError:
    print('DB_PASSWORD environment variable must be defined for this application to work.')
    sys.exit(1)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'PASSWORD': DB_PASSWORD,
        'OPTIONS': {
            'connect_timeout': 5,
        }
    }
}

CONN_MAX_AGE = 120

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth

AUTH_USER_MODEL = "users.ColearnAppUser"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "dashboard"

# Email

try:
    EMAIL_HOST = os.environ['EMAIL_HOST']
except KeyError:
    print('EMAIL_HOST environment variable must be defined to send emails.')
    sys.exit(1)

try:
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
except KeyError:
    print('EMAIL_HOST_USER environment variable must be defined to send emails.')
    sys.exit(1)

try:
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
except KeyError:
    print('EMAIL_HOST_PASSWORD environment variable must be defined to send emails.')
    sys.exit(1)

EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL') if os.environ.get('EMAIL_USE_SSL') else False
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS') if os.environ.get('EMAIL_USE_TLS') else True
EMAIL_PORT = os.environ.get('EMAIL_PORT') if os.environ.get('EMAIL_PORT') else 587
