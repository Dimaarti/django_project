from django.urls import path

from task_manager.models import comments
from .views import HomePageView, CommentsDeleteView, TaskEdit, AttachmentsCreate, TaskView, UserListView, TaskCreateView, AttachmentsView

urlpatterns = [
    path('tasks/', TaskView.as_view(), name = 'tasks'),
    path('users/', UserListView.as_view(), name = 'users'),
    path('', HomePageView.as_view(), name = 'home'),
    path('comments/<int:pk>/delete/', CommentsDeleteView.as_view(), name = 'comments_delete'),
    path('task_create/', TaskCreateView.as_view(), name = 'task_create'),
    path('edit/<int:task_id>', TaskEdit.as_view(), name = 'edit_task'),
    path('create_attachments/', AttachmentsCreate.as_view(), name = 'create_attachments'),
    path('attachments/', AttachmentsView.as_view(), name='attachments'),
]