import os
from decouple import config
def get_app_settings():
    """
    set default settings module or get from environment variable
    """
    setting = os.getenv(
        "DJANGO_SETTINGS_MODULE", "sdtmonitor.settings.production"
    )
    return setting
