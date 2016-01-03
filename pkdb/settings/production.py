from .base import *


DEBUG = False

DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'pkdb',
     }
}


try:
    from .local import *
except ImportError:
    pass
