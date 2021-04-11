from core.settings.development import *

DEBUG = False
ALLOWED_HOSTS = ['0.0.0.0', 'localhost']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CORS_ALLOWED_ORIGINS = [

    "http://localhost:3000",

]
