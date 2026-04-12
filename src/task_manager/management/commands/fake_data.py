import random
from django.core.management.base import BaseCommand
from account.models import User
from task_manager.models import Projects, Tasks, Tags, Comments
from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write("Генерация пользователей")
        users = [
            User(
            username=fake.unique.user_name(),
            email=fake.email()
            )
            for _ in range(100)
        ]
        User.objects.bulk_create(users)
        users = list(User.objects.all())

        self.stdout.write("Генерация проектов")
        projects = [
            Projects(name=fake.company(),
            description=fake.text()
            )
            for _ in range(10)
        ]
        Projects.objects.bulk_create(projects)
        projects = list(Projects.objects.all())

        self.stdout.write("Генерация тегов")

        tags = [
            Tags(
                name=fake.word(),

            )
            for _ in range(20)]
        Tags.objects.bulk_create(tags)
        tags = list(Tags.objects.all())



        self.stdout.write("Генерация задач")
        batch_size = 10000
        for i in range(0, 1000000, batch_size):
            tasks = [
                Tasks(
                    name=fake.sentence(nb_words=4),
                    project=random.choice(projects),
                    assignee=random.choice(users),
                )
            ]
            Tasks.objects.bulk_create(tasks)
            tasks = list(Tasks.objects.all())



            self.stdout.write("Добавление комментариев")
            comments = [
                Comments(task=random.choice(tasks),
                        user=random.choice(users),
                        message=fake.sentence())
                for _ in range(250)
            ]
            Comments.objects.bulk_create(comments)

            self.stdout.write(self.style.SUCCESS('Данные сгенерированы!'))

