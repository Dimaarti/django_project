from django.test import TestCase, Client

from account.models import User
from task_manager.models import Tasks, Attachments


class TestAttachmentsView(TestCase):

    def setUp(self):
        self.client = Client()
        test_user_email = 'test@test.com'
        test_user_password = '1111'
        self.user = User.objects.create_user(
            email=test_user_email,
            password=test_user_password

        )
        self.client.force_login(self.user)

    def test_attachments_list(self):
        path = '/attachments/'
        test_task_name = 'test task'
        test_attachments_name = 'test attachments'
        tasks = Tasks.objects.create(
            name=test_task_name, )

        Attachments.objects.create(
            name=test_attachments_name,
            task=tasks,
        )

        response = self.client.get(path=path)
        objects = response.context['object_list']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0].name, test_attachments_name)
        self.assertEqual(objects[0].task, tasks)
