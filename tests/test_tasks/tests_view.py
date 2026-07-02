from django.test import TestCase, Client

from account.models import User
from task_manager.models import Tasks
from task_manager.models.tasks import TasksStatus


class TestTaskView(TestCase):

    def setUp(self):
        self.client = Client()
        test_user_email = 'test@test.com'
        test_user_password = '1111'
        self.user = User.objects.create_user(
            email=test_user_email,
            password=test_user_password

        )
        self.client.force_login(self.user)

    def test_task_list(self):
        path = '/tasks/'
        test_task_name = 'test task'
        test_default_status = TasksStatus.CREATED
        test_priority = 1

        Tasks.objects.create(
            name=test_task_name,
            priority=test_priority,
            assignee=self.user,
        )

        response = self.client.get(path=path)
        objects = response.context['object_list']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0].name, test_task_name)
        self.assertEqual(objects[0].priority, test_priority)
        self.assertEqual(objects[0].status, test_default_status)
        self.assertEqual(objects[0].assignee, self.user)
