"""
Django settings for agile_web project.
"""

from pathlib import Path
import os  # <--- CRITICAL FIX: Needed for database settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# --- SECURITY CONFIGURATION ---
# In production, pull this from environment variables. 
# For now, we default to the hardcoded one if env var is missing.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-c4i6%3x=$-f#g8mjhp&!q&j-suk@6ye3dm+$gsf3pteuw%(j7y')

# SECURITY WARNING: don't run with debug turned on in production!
# This reads the environment variable "DEBUG". If not set, it defaults to True.
# In Docker, we usually set DEBUG=0 or False.
DEBUG = False

# CRITICAL FIX: Must include your domain and localhost for Docker to work
ALLOWED_HOSTS = [
    'agile-web-services.com', 
    'www.agile-web-services.com', 
    '64.225.22.157',
    'localhost', 
    '127.0.0.1',
    '[::1]' 
]


CSRF_TRUSTED_ORIGINS = [
    "https://agile-web-services.com",
    "https://www.agile-web-services.com",
]

# Tell Django to trust the 'X-Forwarded-Proto' header coming from Nginx/Docker
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# --- APPLICATION DEFINITION ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your Apps
    'main',

    # CRITICAL FIX: Required for Sitemap & SEO features we added
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

# Required for 'django.contrib.sites'
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <--- RECOMMENDED: Handles static files in Docker
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agile_web.urls'

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

WSGI_APPLICATION = 'agile_web.wsgi.application'


# --- DATABASE ---
# Uses environment variables from docker-compose.yml
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'agile_db'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'abcd1234'),
        'HOST': os.environ.get('DB_HOST', 'localhost'), # 'db' in docker, 'localhost' locally
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}


# --- PASSWORD VALIDATION ---
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- STATIC FILES (CSS, JavaScript, Images) ---
STATIC_URL = '/static/'

# CRITICAL FIX: Tells Django where to put files when you run 'collectstatic'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Optional: Enable WhiteNoise compression and caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# --- DEFAULT AUTO FIELD ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- EMAIL SETTINGS ---
# Note: In production, change this to 'smtp.EmailBackend' to send real emails.
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
# DEFAULT_FROM_EMAIL = 'noreply@agile-web-services.com'
# ADMIN_EMAIL = 'admin@agile-web-services.com'

# --- EMAIL SETTINGS ---
# If EMAIL_HOST_USER is in .env, use SMTP (Gmail). Otherwise, print to console.
if os.environ.get('EMAIL_HOST_USER'):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
else:
    # Fallback for development
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'noreply@agile-web-services.com'
ADMIN_EMAIL = 'admin@agile-web-services.com'