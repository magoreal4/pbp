from .base import *
import environ

env = environ.Env()

environ.Env.read_env()

DEBUG = False

SECRET_KEY = env.str("SECRET_KEY")

ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# SECRET_KEY = env.str("SECRET_KEY")

# ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))

# Database PostgreSQL
# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get("SQL_ENGINE"),
#         'NAME': os.environ.get("SQL_DATABASE"),
#         'USER': os.environ.get("SQL_USER"),
#         'PASSWORD': os.environ.get("SQL_PASSWORD"),
#         'HOST': os.environ.get("SQL_HOST"),
#         'PORT': os.environ.get("SQL_PORT"),
#     }
# }

try:
    from .local import *
except ImportError:
    pass
