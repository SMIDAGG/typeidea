from .base import *

DEBUG = True
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER':'root',
        'PASSWORD':'64301034',
        'HOST':'localhost'
    }
}