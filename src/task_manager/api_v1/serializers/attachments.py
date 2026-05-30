from rest_framework import serializers

from task_manager.models import Attachments


class AttachmentsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Attachments
        fields = ["id", "name", "file", "photo"]
