from django.apps import AppConfig


class BoostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boosts'

    def ready(self):
        import boosts.signals
