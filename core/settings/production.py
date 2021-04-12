from core.settings.development import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0',
                 'localhost', 'https://engmedapp.herokuapp.com']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CORS_ALLOWED_ORIGINS = [

    "http://localhost:3000",

]
