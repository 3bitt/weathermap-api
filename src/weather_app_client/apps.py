import os
from django.apps import AppConfig


class WeatherAppClientConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "weather_app_client"
    
    def ready(self):
        from . import scheduler
        if os.environ.get("RUN_MAIN", None) != "true":
            scheduler.start_scheduler()