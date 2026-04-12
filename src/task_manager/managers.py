from django.db import models


class TaskQuerySet(models.QuerySet):

    def status(self):
        return self.filter(status='completed')


class TaskManager(models.Manager):

    def get_queryset(self):
        return TaskQuerySet(self.model, using=self._db)

    def status_completed(self):
        return self.get_queryset().status()
