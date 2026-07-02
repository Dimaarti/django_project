from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from task_manager.models import comments
from .api_v1.views.tasks import TasksViewSet
from .api_v1.views.users import UsersViewSet
from .views import HomePageView, CommentsDeleteView, TaskEdit, AttachmentsCreate, TaskView, UserListView, \
    TaskCreateView, AttachmentsView, user_tasks

routing = DefaultRouter()
routing.register('tasks', TasksViewSet)
routing.register('users', UsersViewSet)

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('users/', UserListView.as_view(), name='users'),
    path('', HomePageView.as_view(), name='home'),
    path('comments/<int:pk>/delete/', CommentsDeleteView.as_view(), name='comments_delete'),
    path('task_create/', TaskCreateView.as_view(), name='task_create'),
    path('edit/<int:task_id>', TaskEdit.as_view(), name='edit_task'),
    path('create_attachments/', AttachmentsCreate.as_view(), name='create_attachments'),
    path('attachments/', AttachmentsView.as_view(), name='attachments'),
    path('api/', include('task_manager.api_v1.urls')),
    path('api/', include(routing.urls)),
    path('users/<int:pk>/', user_tasks, name='user_tasks'),
]
