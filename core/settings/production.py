from core.settings.development import *
import dj_database_url

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

DEBUG = False
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['api.engmedapp.com', '127.0.0.1', '0.0.0.0',
                 'localhost', 'engmedapp.herokuapp.com']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOWED_ORIGINS = [
#     "https://engmedapp.com",
#     "https://www.engmedapp.com",
#     "http://localhost:8000",
#     "http://127.0.0.1:8000"
# ]

USE_S3 = True

REST_SOCIAL_OAUTH_ABSOLUTE_REDIRECT_URI = 'https://engmedapp.com/auth/social/google'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
