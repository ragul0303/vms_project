# apps.py

from django.apps import AppConfig

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vms_app'

    def ready(self):
        import vms_app.signals  # This will import signals and connect them when the app is ready
