from django.urls import path
from task_manager.views import index, tasks, users, home

urlpatterns = [
    path('', index, name = 'tasks'),
    path('tasks/', tasks, name = 'tasks'),
    path('users/', users, name = 'users'),
    path('home/', home, name = 'home'),
]