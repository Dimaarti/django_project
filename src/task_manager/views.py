from django.shortcuts import render
from django.http import HttpResponse
from task_manager.models import Tasks
from account.models import User
from task_manager.models.tasks import EducationTasks

#MTV
# def index(request):
#     return HttpResponse("<h1>Hello, world.</h1>")

def index(request):
    return render(request, "home.html")

def tasks(request):
    context = {
        "tasks": Tasks.objects.select_related("assignee").prefetch_related("comments").all()
    }
    return render(request, "tasks.html", context = context)

def users(request):
    context = {
        "users": User.objects.all(),
    }
    return render(request, "users.html", context = context)

def home(request):
    return render(request, "home.html")

