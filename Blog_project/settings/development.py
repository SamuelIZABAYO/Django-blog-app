from Blog_project.settings.base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']
# INSTALLED_APPS += [
#     'debug_toolbar',
# ]
# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
