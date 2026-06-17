import django_filters
from django_filters import filters
from rest_framework import serializers
from rest_framework.response import Response

from account.models import User
from config.models import BaseModel
from task_manager.models import *


class TasksCreatedFilter(django_filters.FilterSet):
    # created_at__gte = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    # created_at__lte= django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    # priority = django_filters.NumberFilter(field_name='priority', lookup_expr='exact')
    # status = django_filters.CharFilter(field_name='status', lookup_expr='exact')
    class Meta:
        model = Tasks
        fields = {'created_at': ['gte', 'lte'],
                  'priority': ['exact'],
                  'status': ['exact'],
                  }


class TasksSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=False, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=100)
    priority = serializers.IntegerField(required=False, allow_null=True)
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    def create(self, validated_data):
        return Tasks.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.priority = validated_data.get("priority", instance.priority)
        instance.save()
        return instance
