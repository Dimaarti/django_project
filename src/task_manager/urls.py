from django.urls import path

from task_manager.models import comments
from .views import index, tasks, users, home, comments_adding, task_create, edit_task, attachments, create_attachments

urlpatterns = [
    path('', index, name = 'tasks'),
    path('tasks/', tasks, name = 'tasks'),
    path('users/', users, name = 'users'),
    path('home/', home, name = 'home'),
    path('comments/<int:task_id>', comments_adding, name = 'comments_adding'),
    path('task_create/', task_create, name = 'task_create'),
    path('edit/<int:task_id>', edit_task, name = 'edit_task'),
    path('create_attachments/', create_attachments, name = 'create_attachments'),
    path('attachments/', attachments, name='attachments'),
]