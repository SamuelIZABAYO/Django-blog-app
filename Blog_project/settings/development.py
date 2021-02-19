DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'TestDjango',
        'USER': 'postgres',
        'PASSWORD': '12',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
ALLOWED_HOSTS = ['*']
try:
    from Blog_project.settings.base import *
except Exception as e:
    pass
