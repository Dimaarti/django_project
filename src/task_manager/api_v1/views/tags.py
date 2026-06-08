from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from task_manager.api_v1.serializers.tags import TagsSerializer
from task_manager.models import Tags


@extend_schema(tags=["Tags"])
@api_view(["GET", "POST"])
def tags_list(request):
    if request.method == "GET":
        tasks = Tags.objects.all()
        serializer = TagsSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
