from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

SECRET_KEY = env('DJANGO_SECRET_KEY', default='yp6kgx9wxp#qlu2!)jx=@&!f@!92a6q-bb=_qq(x0)khsc784)')