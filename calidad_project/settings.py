import os
from pathlib import Path

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'django-insecure-reemplaza-esto-con-tu-clave'
DEBUG = True
ALLOWED_HOSTS = ['https://calidad-project.onrender.com',
                 'localhost',
                 '127.0.0.1',]

# APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestion',
    'widget_tweaks',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT URL
ROOT_URLCONF = 'calidad_project.urls'

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'gestion' / 'templates'],
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

# WSGI
WSGI_APPLICATION = 'calidad_project.wsgi.application'

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PASSWORD VALIDATORS
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

# LANGUAGE / TIME
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = 'static/'
#STATICFILES_DIRS = [BASE_DIR / 'static']

# MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# DEFAULT PRIMARY KEY FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN / LOGOUT
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'ver_lotes'
LOGOUT_REDIRECT_URL = 'login'

AUTH_USER_MODEL = 'gestion.Usuario'

if os.environ.get('RENDER'):
    DEBUG = False
    ALLOWED_HOSTS = ['tu-nombre-del-servicio.onrender.com']

# Asegúrate de tener configurado el uso de archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# CUSTOM USER MODEL (opcional, si lo tienes implementado)
# AUTH_USER_MODEL = 'gestion.UsuarioPersonalizado'
