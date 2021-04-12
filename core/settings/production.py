from core.settings.development import *
import dj_database_url

DATABASES = {

}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0',
                 'localhost', 'engmedapp.herokuapp.com']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CORS_ALLOWED_ORIGINS = [

    "http://localhost:3000",

]
