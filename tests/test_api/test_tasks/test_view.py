from rest_framework import status
from rest_framework.test import APITestCase

from account.models import User
from task_manager.models import Tasks


class TestTaskApiView(APITestCase):

    def setUp(self):
        test_user_email = 'test@test.com'
        test_user_password = '1111'
        self.user = User.objects.create_user(
            email=test_user_email,
            password=test_user_password

        )
        self.client.force_login(self.user)

        self.test_task_name = 'test api task'
        self.test_priority = 1

        Tasks.objects.create(
            name=self.test_task_name,
            priority=self.test_priority,
            assignee=self.user,
        )

    def test_list_api_task(self):
        path = '/api/tasks/'

        response = self.client.get(path)

        task = response.json()['results'][0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(task['name'], self.test_task_name)
        self.assertEqual(task['priority'], self.test_priority)
        self.assertEqual(task['assignee'], self.user.id)

    def test_create_api_task(self):
        Tasks.objects.filter(name="test api task").delete()
        path = '/api/tasks/'
        body = {
            'name': self.test_task_name,
            'priority': self.test_priority,
            'assignee': self.user.id,
        }
        response = self.client.post(path, body, format='json')
        task = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(task['name'], self.test_task_name)
        self.assertEqual(task['priority'], self.test_priority)
        self.assertEqual(task['assignee'], self.user.id)

    def test_update_api_task(self):
        task = Tasks.objects.get(name=self.test_task_name)
        path = f'/api/tasks/{task.id}/'
        body = {
            'name': self.test_task_name,
            'priority': self.test_priority,
            'assignee': self.user.id,
        }
        response = self.client.put(path, body, format='json')

        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['name'], self.test_task_name)
        self.assertEqual(data['priority'], self.test_priority)
        self.assertEqual(data['assignee'], self.user.id)

    def test_delete_api_task(self):
        task = Tasks.objects.get(name=self.test_task_name)
        path = f'/api/tasks/{task.id}/'
        response = self.client.delete(path)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
