from core.settings.development import *
import dj_database_url

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0',
                 'localhost', 'engmedapp.herokuapp.com']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CORS_ALLOWED_ORIGINS = [

    "https://lucid-visvesvaraya-8a085a.netlify.app",
    "https://engmedapp.com",
    "https://www.engmedapp.com",

]
