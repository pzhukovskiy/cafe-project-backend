from django.apps import AppConfig


class FeedbackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #type: ignore
    name = 'feedback'
    verbose_name = 'Обратная связь'
