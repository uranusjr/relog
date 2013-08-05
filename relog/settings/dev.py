from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = str(PROJECT_ROOT['media'])
STATIC_ROOT = str(PROJECT_ROOT['static'])

ADMIN_URL_PREFIX = 'admin'

# Log EVERYTHING to console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG'
        }
    }
}
