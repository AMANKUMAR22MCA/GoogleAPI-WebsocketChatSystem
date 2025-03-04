"""
Django settings for google_apis project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1goje3gr@e5f3rrm&kz1q0yvmm09oo6ib%#s=4wfo_d^)@l-pi'

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
    "corsheaders",
    'django.contrib.staticfiles',
    'api_app',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    "channels",
    "chat", 
]
SITE_ID = 2


# INSTALLED_APPS += ['csp']

# CSP_DEFAULT_SRC = ["'self'", "https://apis.google.com", "https://accounts.google.com"]
# CSP_SCRIPT_SRC = ["'self'", "https://apis.google.com", "https://accounts.google.com", "'unsafe-inline'"]
# CSP_STYLE_SRC = ["'self'", "'unsafe-inline'", "https://fonts.googleapis.com"]
# CSP_FRAME_SRC = ["'self'", "https://drive.google.com", "https://accounts.google.com", "https://content.googleapis.com"]


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Just this backend for normal auth
    'allauth.account.auth_backends.AuthenticationBackend'
)
# JWT settings for sessionless auth
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

GOOGLE_CLIENT_ID = ""
GOOGLE_CLIENT_SECRET = ""
GOOGLE_REDIRECT_URI = "http://localhost:8000/auth/callback/"
GOOGLE_SCOPES = ["openid", "email", "profile", "https://www.googleapis.com/auth/drive"]
# GOOGLE_SIGNIN_REDIRECT_URI = "http://localhost:8000/auth/callback/"
GOOGLE_DRIVE_REDIRECT_URI = "http://localhost:8000/google-drive/callback/"

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_HTTPONLY':False,
    'JWT_AUTH_RETURN_EXPIRATION':True
}

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'APP': {
#             'client_id': GOOGLE_CLIENT_ID,
#             'secret': GOOGLE_CLIENT_SECRET,
#         },
#     }
# }

GOOGLE_LOGIN_REDIRECT_URL = 'https://accounts.google.com/o/oauth2/v2/auth?redirect_uri={GOOGLE_REDIRECT_URI}&prompt=consent&response_type=code&client_id={GOOGLE_CLIENT_ID}&scope=openid%20email%20profile&access_type=offline'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # "google_apis.middleware.CSPMiddleware",
    'allauth.account.middleware.AccountMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
X_FRAME_OPTIONS = "ALLOWALL"
X_FRAME_OPTIONS = "ALLOW-FROM https://drive.google.com"
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "https://accounts.google.com",  # Allow Google OAuth requests
]
CSRF_TRUSTED_ORIGINS = [
    "https://accounts.google.com",
    "https://apis.google.com",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

ROOT_URLCONF = 'google_apis.urls'

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

WSGI_APPLICATION = 'google_apis.wsgi.application'
# WSGI_APPLICATION = "api_app.wsgi.application"

import pymysql
pymysql.install_as_MySQLdb()
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'google_urls',       # Your database name
        'USER': 'root',       # Your MySQL username
        'PASSWORD': 'Aman@2000',  # Your MySQL password
        'HOST': '127.0.0.1',          # Or the address of your MySQL server
        'PORT': '3306',               # Default MySQL port
    }
}
# websocket 

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",  # Use Redis for production
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
