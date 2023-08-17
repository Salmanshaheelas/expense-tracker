from .common import *

DEBUG = True

SECRET_KEY = "django-insecure-5^p+!=0u))*vz6g1vl67(f6)1ta-)_6mtmn+j^$w@k-ku&9u@+"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'expensetracker',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Faris@123'
    }
}

CELERY_BROKER_URL = 'redis://localhost:6379/0'

EMAIL_HOST = 'smtp.gmail.com'  # Example: smtp.gmail.com
EMAIL_PORT = 587  # Port number for your email host
EMAIL_HOST_USER = 'salmanshaheelas@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'rtiygzmuelwauyvq'  # Your email password
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False