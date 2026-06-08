from drf_spectacular.utils import extend_schema
from rest_framework import status, mixins, generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from task_manager.api_v1.serializers.projects import ProjectsSerializer
from task_manager.models import Projects

@extend_schema(tags=["Projects"])
class ProjectsList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@extend_schema(tags=["Projects"])
class ProjectsDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)