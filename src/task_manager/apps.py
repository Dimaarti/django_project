from django.apps import AppConfig
from django.db.models.signals import post_save


class TaskManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_manager'
    verbose_name = 'Менеджер задач'

    def ready(self):
        from task_manager.signals import my_add_comment


