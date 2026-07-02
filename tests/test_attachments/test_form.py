from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client

from account.models import User
from task_manager.models import Tasks, Attachments
from task_manager.models.tasks import TasksStatus


class TestAttachmentsForm(TestCase):

    def setUp(self):
        self.client = Client()
        test_user_email = 'test@test.com'
        test_user_password = '1111'
        self.user = User.objects.create_user(
            email=test_user_email,
            password=test_user_password

        )
        self.client.force_login(self.user)

    def test_attachments_create(self):
        path = '/create_attachments/'
        test_task_name = 'test task'
        test_attachments_name = 'test attachment'
        tasks = Tasks.objects.create(
            name=test_task_name,
        )

        body = {
            'name': test_attachments_name,
            'task': tasks.id,
        }

        response = self.client.post(
            path=path,
            data=body
        )
        self.assertEqual(response.status_code, 302)

        attachments = Attachments.objects.all()

        self.assertEqual(len(attachments), 1)
        self.assertEqual(attachments[0].name, test_attachments_name)
        self.assertEqual(attachments[0].task, tasks)
