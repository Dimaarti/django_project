from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import PermissionsMixin
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from task_manager.api_v1.serializers.tasks import TasksSerializer
from task_manager.models import Tasks


# @csrf_exempt
# def tasks_list(request):
#     if request.method == "GET":
#         tasks = Tasks.objects.all()
#         serializer = TasksSerializer(tasks, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = TasksSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @api_view(["GET", "POST"])
# def tasks_list(request):
#     if request.method == "GET":
#         tasks = Tasks.objects.all()
#         serializer = TasksSerializer(tasks, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = TasksSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @extend_schema(tags=["Tasks"])
# class TasksListAPIView(APIView):
#     @extend_schema(
#         responses={200: TasksSerializer(many=True)},
#     )
#     def get(self, request, format=None):
#         tasks = Tasks.objects.all()
#         serializer = TasksSerializer(tasks, many=True)
#         return Response(serializer.data)
#     @extend_schema(
#         request=TasksSerializer,
#         responses={201: TasksSerializer(many=True)},
#     )
#     def post(self, request, format=None):
#         serializer = TasksSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @extend_schema(tags=['TasksDetail'])
# class TasksDetailAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Tasks.objects.get(pk=pk)
#         except Tasks.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         tasks = self.get_object(pk)
#         serializer = TasksSerializer(tasks)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         tasks = self.get_object(pk)
#         serializer = TasksSerializer(tasks, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         tasks = self.get_object(pk)
#         tasks.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(tags=["Tasks"])
class TasksViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAdminUser]



