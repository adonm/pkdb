from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#_+c((#jrq=c78h3@2_78oj*awxzr-r05(!6ro7#w9(d=yw6rx'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'pkdb-dev',
     }
}

try:
    from .local import *
except ImportError:
    pass
