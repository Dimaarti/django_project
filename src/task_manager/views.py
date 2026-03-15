from django.shortcuts import render
from django.http import HttpResponse

#MTV
# def index(request):
#     return HttpResponse("<h1>Hello, world.</h1>")

def index(request):
    return render(request, "home.html")

def tasks(request):
    task = [
        {"task_name": "Fix login bug", "status": "in progress", "priority": "high"},
        {"task_name": "Create navbar", "status": "done", "priority": "medium"},
        {"task_name": "Write tests", "status": "todo", "priority": "high"},
        {"task_name": "Update documentation", "status": "todo", "priority": "low"},
        {"task_name": "Deploy project", "status": "in progress", "priority": "medium"}
    ]
    context = {
        "tasks": task,
    }
    return render(request, "tasks.html", context = context)

def users(request):
    user = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 28},
        {"name": "Diana", "age": 22}
    ]
    context = {
        "users": user
    }
    return render(request, "users.html", context = context)

def home(request):
    return render(request, "home.html")

