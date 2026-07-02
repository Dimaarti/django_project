from django.test import TestCase, Client

from account.models import User
from task_manager.models import Tasks
from task_manager.models.tasks import TasksStatus


class TestTaskForm(TestCase):

    def setUp(self):
        self.client = Client()
        test_user_email = 'test@test.com'
        test_user_password = '1111'
        self.user = User.objects.create_user(
            email=test_user_email,
            password=test_user_password

        )
        self.client.force_login(self.user)

    def test_task_create(self):
        path = '/task_create/'
        test_task_name = 'test task'
        test_description = 'test description'
        test_priority = 3
        test_status = TasksStatus.CREATED

        body = {
            'name': test_task_name,
            'description': test_description,
            'priority': test_priority,
            'status': test_status,
        }

        response = self.client.post(
            path=path,
            data=body
        )
        self.assertEqual(response.status_code, 302)

        tasks = Tasks.objects.all()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].name, test_task_name)
        self.assertEqual(tasks[0].description, test_description)
        self.assertEqual(tasks[0].priority, test_priority)
        self.assertEqual(tasks[0].status, test_status)
