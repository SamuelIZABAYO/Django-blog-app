import environ

env = environ.Env(DEBUG=(bool, False))
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['peaceful-headland-57859.herokuapp.com']
# DATABASES = {'default': env.db(), }
