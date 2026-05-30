from drf_spectacular.utils import extend_schema

from task_manager.api_v1.serializers.attachments import AttachmentsSerializer
from task_manager.models import Attachments
from task_manager.api_v1.serializers import attachments
from rest_framework import mixins
from rest_framework import generics

@extend_schema(tags=["Attachments"])
class AttachmentsList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@extend_schema(tags=["Attachments"])
class AttachmentsDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)