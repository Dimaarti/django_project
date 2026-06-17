from rest_framework import serializers

from account.models import User


class UsersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)
    class Meta:
        model = User
        fields = ["id", "email"]