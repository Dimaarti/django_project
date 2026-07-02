

from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models.users import User
from config.pagination import UsersListPagination
from task_manager.api_v1.serializers.users import UsersSerializer
from task_manager.models import Tasks



@extend_schema(tags=["Users"])
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    pagination_class = UsersListPagination