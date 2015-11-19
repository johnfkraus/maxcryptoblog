# var_www_johnfkraus_pythonanywhere_com_wsgi.py

import os
import sys

path = '/home/johnfkraus/maxcryptoblog'  # use your own username here
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'allauthdemo.settings'

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())
