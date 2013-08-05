from .base import *

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'relog',
        'USER': 'relog_django',
        'PASSWORD': get_environ('RELOG_DJANGO_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = get_environ('RELOG_SECRET_KEY')

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/var/www/relog/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/var/www/relog/static/'

# The prefix that is added to all admin-related URLs. This makes the admin site
# safe from brute-force admin site attacks.
ADMIN_URL_PREFIX = get_environ('RELOG_ADMIN_URL')
