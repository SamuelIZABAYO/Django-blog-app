import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': dj_database_url.config()
}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PHOTO', 'https')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2'
    }
}
try:
    from local_settings import *
except Exception as e:
    pass
