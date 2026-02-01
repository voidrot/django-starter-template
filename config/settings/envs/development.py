from config.settings.components.base import *  # noqa: F403
from config.settings.components.base import MIDDLEWARE, INSTALLED_APPS

DEBUG = True

INSTALLED_APPS += ["zeal"]
MIDDLEWARE += ["zeal.middleware.zeal_middleware"]

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# Print emails to console
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Disable manifest storage in development to avoid running collectstatic
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
