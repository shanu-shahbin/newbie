
import smtplib
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-(!@rd#t*o-13arq$+mu024+%awip#-tl7qon^i^$=h6y@-6!67'


DEBUG = True

ALLOWED_HOSTS = ['www.newbieos.in', 'newbieos.in']



INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'app',
    'ckeditor',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]

AUTHENTICATION_BACKENDS = [
    
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth backend
    'app.backends.EmailBackend',  # Replace 'yourapp' with the correct app name
    'django.contrib.auth.backends.ModelBackend',  # Keep the default backend as a fallback
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware", 
]


JAZZMIN_SETTINGS = {
    'site_header': 'NewbieOs Admin',
    'site_brand': 'NewbieOs',
    "welcome_sign": "Welcome to the admin dashboard",
    "show_ui_builder": True,
    "navigation_expanded": True,  
    }

ROOT_URLCONF = 'newbieos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add your templates directory here
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


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id':'43074578158-plta42kh56rmc9a5jk02qq70s4dljm3n.apps.googleusercontent.com',
            'secret': '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',
          
        },
        'SCOPE': ['profile','email',],
         'AUTH_PARAMS': {'access_type': 'online'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': True,
    },
    'github': {
        'APP': {
            'client_id': 'Ov23liPRyGWdfAcezLZL',
            'secret': '77928bf94fbef9220829c58d0d7d5b4741ad641a',
           
        }
    }
   
}

SOCIALACCOUNT_LOGIN_ON_GET=True
LOGIN_REDIRECT_URL = 'index'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django_errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True



WSGI_APPLICATION = 'newbieos.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
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

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOGIN_URL = 'login'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR,  'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'newbieos.contact@gmail.com'
EMAIL_HOST_PASSWORD = 'rged vvor jtdk pxhk'
DEFAULT_FROM_EMAIL = 'newbieos.contact@gmail.com'
ADMIN_EMAIL = 'newbieos.contact@gmail.com'  

try:
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    print("SMTP connection successful")
    server.quit()
except smtplib.SMTPAuthenticationError:
    print("Failed to authenticate with the SMTP server. Please check the username or password.")
except smtplib.SMTPConnectError:
    print("Failed to connect to the SMTP server.")
except Exception as e:
    print(f"SMTP connection failed: {e}")
