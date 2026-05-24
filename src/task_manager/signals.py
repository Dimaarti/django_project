import os
from linecache import cache

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from task_manager.forms import TaskForm
from task_manager.models import Tasks, Comments, Attachments


@receiver(post_save, sender=Tasks)
def my_add_comment(sender, instance, created, **kwargs):
    if created:
        Comments.objects.create(
            task=instance,
            message="Task created"
        )


@receiver(post_delete, sender=Attachments)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()


@receiver([post_save, post_delete], sender=TaskForm)
def cache_clear(sender, instance, **kwargs):
    cache.clear()
