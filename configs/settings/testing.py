import os
from .settings import *

DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
