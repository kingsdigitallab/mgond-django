from .base import *  # noqa

INTERNAL_IPS = INTERNAL_IPS + ['']
ALLOWED_HOSTS = ['']

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'NAME': 'app_mgond_liv',
        'USER': 'app_mgond',
        'PASSWORD': '',
        'HOST': ''
    },
}
