

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from task_manager.models import Tasks, Comments
from account.models import User
from task_manager.models.tasks import EducationTasks
from .forms import CommentForm, TaskForm


# MTV
# def index(request):
#     return HttpResponse("<h1>Hello, world.</h1>")

def index(request):
    return render(request, "home.html")


def tasks(request):
    context = {
        "tasks": Tasks.objects.select_related("assignee").prefetch_related("comments").all()
    }
    return render(request, "tasks.html", context=context)


def users(request):
    context = {
        "users": User.objects.all(),
    }
    return render(request, "users.html", context=context)


def home(request):
    return render(request, "home.html")


def comments_adding(request, task_id):
    task = Tasks.objects.get(id=task_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comments.objects.create(task=task, message=form.cleaned_data.get("message"))
        return redirect("tasks")
    else:
        form = CommentForm()

    return render(request, "comments_adding.html", {"form": form, "task": task})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/tasks/")
    else:
        form = TaskForm()

    return render(request, "task_create.html", {"form": form})


def edit_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks")
    else:
        form = TaskForm(instance=task)

    return render(request, "edit_task.html", {"form":form, "task":task})


