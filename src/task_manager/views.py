from django.core.paginator import Paginator
from django.db import transaction
from django.db.transaction import atomic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe

from task_manager.models import Tasks, Comments, Attachments
from account.models import User
from task_manager.models.tasks import EducationTasks
from .forms import CommentForm, TaskForm, AttachmentsForm
from pathlib import Path
from django.core.files import File


# MTV
# def index(request):
#     return HttpResponse("<h1>Hello, world.</h1>")

def index(request):
    return render(request, "home.html")


def tasks(request):
    task = Tasks.objects.select_related("assignee").prefetch_related("comments").all()
    paginator = Paginator(task, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "tasks": page_obj,
        "page_obj": page_obj,
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


@transaction.atomic
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            comments_list = request.POST.getlist("comments")
            (Comments.objects.bulk_create([
                Comments
                (task=task,
                 message=message
                 )
                for message in comments_list
            ])
            )
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

    return render(request, "edit_task.html", {"form": form, "task": task})


def attachments(request):
    attachment = Attachments.objects.prefetch_related("task").all()
    paginator = Paginator(attachment, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "attachments": page_obj,
        "page_obj": page_obj,
    }
    return render(request, "attachments.html", context=context)


# def create_attachments(request):
#     if request.method == "POST":
#         form = AttachmentsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect("attachments")
#     else:
#         form = AttachmentsForm()
#
#     return render(request, "task_attachments.html", {"form": form})


#
def save_attachments(file_path, task_id):
    path = Path(file_path)
    task = Tasks.objects.get(id=task_id)
    attachment = Attachments(task=task, name=path.name)
    with path.open(mode="rb") as f:
        attachment.file.save(
            path.name,
            File(f),
            save=True
        )
    return attachment

def create_attachments(file_path, task_id):
    save_attachments("media_files/spacs.pdf", task_id=4)
    return redirect("attachments")

