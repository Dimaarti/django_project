from django.db.models.signals import post_save
from django.dispatch import receiver
from task_manager.models import Tasks, Comments


@receiver(post_save, sender=Tasks)

def my_add_comment(sender, instance, created, **kwargs):
    if created:
        Comments.objects.create(
            task=instance,
            message="Task created"
        )


