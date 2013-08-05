from .dev import *


ADMINS = (
    ('Tzu-ping Chung', 'uranusjr@gmail.com')
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'relog',
        'USER': 'relog_django',
        'PASSWORD': 'sdfum0e[u4[0238y5h3245',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = 'h=$1xeu+vmawkv_wv$7r6vi@p!*@gic0+v$)r+o_*md^(4tgr8'
