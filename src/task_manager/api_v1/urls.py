from django.urls import path
from rest_framework.routers import DefaultRouter

from task_manager.api_v1.views.attachments import AttachmentsList, AttachmentsDetail
from task_manager.api_v1.views.comments import CommentsList, CommentsDetail
from task_manager.api_v1.views.projects import ProjectsList, ProjectsDetail
from task_manager.api_v1.views.tags import tags_list
from task_manager.api_v1.views.tasks import TasksViewSet
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path("tasks/", TasksListAPIView.as_view()),
    # path("tasks/<int:pk>/", TasksDetailAPIView.as_view()),
    path("attachments/", AttachmentsList.as_view()),
    path("attachments/<int:pk>", AttachmentsDetail.as_view()),
    path("tags/", tags_list),
    path('comments/', CommentsList.as_view()),
    path('comments/<int:pk>', CommentsDetail.as_view()),
    path('projects/', ProjectsList.as_view()),
    path('projects/<int:pk>', ProjectsDetail.as_view()),
]
