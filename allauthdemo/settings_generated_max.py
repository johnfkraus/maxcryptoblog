"""
Django settings for allauthdemo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# print('BASE_DIR = ', BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'bootstrap3',  # optional module for making bootstrap forms easier
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauthdemo.auth',
    'allauthdemo.demo',
    # 'shell_plus',
)

# print(type(INSTALLED_APPS))   class: tuple

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'allauthdemo.urls'

WSGI_APPLICATION = 'allauthdemo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# pythonanywhere says STATICFILES_DIRS should not contain the STATIC_ROOT setting
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "blog/static"),
)

# Authentication

AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        # allauth templates: you could copy this directory into your
        # project and tweak it according to your needs
        # os.path.join(PROJECT_ROOT, 'templates', 'uniform', 'allauth'),
        # example project specific templates
        os.path.join(BASE_DIR, 'allauthdemo', 'templates', 'plain', 'example'),
        # os.path.join(BASE_DIR, 'allauthdemo', 'templates', 'bootstrap', 'allauth'),
        os.path.join(BASE_DIR, 'allauthdemo', 'templates', 'allauth'),
        os.path.join(BASE_DIR, 'allauthdemo', 'templates'),
        os.path.join(BASE_DIR, 'templates'),
        os.path.join(BASE_DIR, 'blog', 'templates'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            # needed for admin templates
            'django.contrib.auth.context_processors.auth',
            # these *may* not be needed
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.contrib.messages.context_processors.messages',
            # allauth needs this from django
            'django.template.context_processors.request',
            'blog.context_processors.app_title',
            # allauth specific context processors
            # 'allauth.account.context_processors.account',
            # 'allauth.socialaccount.context_processors.socialaccount',
        ],
    },
}]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 2
AUTH_USER_MODEL = 'allauthdemo_auth.DemoUser'
LOGIN_REDIRECT_URL = '/member/'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
# ACCOUNT_EMAIL_VERIFICATION = 'none'  # testing...
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
SOCIALACCOUNT_AUTO_SIGNUP = False  # require social accounts to use the signup form ... I think
# For custom sign-up form:
# http://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth


# print('BASE_DIR = ', BASE_DIR)
# print('STATICFILES_DIRS = ', STATICFILES_DIRS)


ALLOWED_HOSTS = [
    'johnfkraus.pythonanywhere.com',  # Allow domain and subdomains
    'http://localhost:8000',
]
