from linecache import cache
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db import transaction
from django.db.transaction import atomic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView
from django.views.generic.list import ListView

from task_manager.models import Tasks, Comments, Attachments
from account.models import User
from task_manager.models.tasks import EducationTasks
from .forms import CommentForm, TaskForm, AttachmentsForm
from pathlib import Path
from django.core.files import File


# MTV
# def index(request):
#     return HttpResponse("<h1>Hello, world.</h1>")

# def index(request):
#     return render(request, "home.html")


# def tasks(request):
#     task = Tasks.objects.select_related("assignee").prefetch_related("comments", "attachments").all()
#     paginator = Paginator(task, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         "tasks": page_obj,
#         "page_obj": page_obj,
#     }
#     return render(request, "tasks.html", context=context)
#


class TaskView(ListView):
    template_name = "tasks.html"
    model = Tasks
    paginate_by = 10
    paginator_class = Paginator
    queryset = Tasks.objects.select_related("assignee").prefetch_related("comments", "attachments").all()

    def get_context_data(self, **kwargs):
        context = super(TaskView, self).get_context_data(**kwargs)
        page_number = self.request.GET.get("page")
        paginator = self.paginator_class(self.queryset, self.paginate_by)
        context["tasks"] = paginator.get_page(page_number)
        context["page_obj"] = paginator.get_page(page_number)
        return context


# def users(request):
#     context = {
#         "users": User.objects.all(),
#     }
#     return render(request, "users.html", context=context)

@method_decorator(
    cache_page(60*10, cache="redis_cache"), name="dispatch")
class UserListView(ListView):
    model = User
    template_name = "users.html"
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context["users"] = self.queryset
        return context

@method_decorator(cache_page(60*30, cache="db_cache"), name="dispatch")
class HomePageView(TemplateView):
    template_name = "home.html"


# def comments_adding(request, task_id):
#     task = Tasks.objects.get(id=task_id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             Comments.objects.create(task=task, message=form.cleaned_data.get("message"))
#         return redirect("tasks")
#     else:
#         form = CommentForm()
#
#     return render(request, "comments_delete.html", {"form": form, "task": task})

class CommentsDeleteView(LoginRequiredMixin, DeleteView):
    model = Comments
    template_name = "comments_delete.html"
    success_message = "Comment deleted successfully"
    success_url = reverse_lazy("tasks")


# @transaction.atomic
# def task_create(request):
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save()
#             comments_list = request.POST.getlist("comments")
#             (Comments.objects.bulk_create([
#                 Comments
#                 (task=task,
#                  message=message
#                  )
#                 for message in comments_list
#             ])
#             )
#             return redirect("/tasks/")
#     else:
#         form = TaskForm()
#
#     return render(request, "task_create.html", {"form": form})



class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = "task_create.html"
    success_url = reverse_lazy("tasks")


# def edit_task(request, task_id):
#     task = Tasks.objects.get(id=task_id)
#     if request.method == "POST":
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect("tasks")
#     else:
#         form = TaskForm(instance=task)
#
#     return render(request, "edit_task.html", {"form": form, "task": task})


class TaskEdit(CreateView, Tasks):
    form_class = TaskForm
    template_name = "edit_task.html"
    success_url = reverse_lazy("tasks")

    def get_context_data(self, **kwargs):
        context = super(TaskEdit, self).get_context_data(**kwargs)
        context["task"] = Tasks.objects.get(id=self.kwargs["task_id"])
        return context


# def attachments(request):
#     attachment = Attachments.objects.prefetch_related("task").all()
#     paginator = Paginator(attachment, 10)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     context = {
#         "attachments": page_obj,
#         "page_obj": page_obj,
#     }
#     return render(request, "attachments.html", context=context)

class AttachmentsView(ListView):
    template_name = "attachments.html"
    model = Attachments
    context_object_name = "attachment"
    paginate_by = 10
    paginator_class = Paginator
    queryset = Attachments.objects.prefetch_related("task").all()

    def get_context_data(self, **kwargs):
        context = super(AttachmentsView, self).get_context_data(**kwargs)
        page_number = self.request.GET.get("page")
        paginator = self.paginator_class(self.queryset, self.paginate_by)
        context["attachments"] = paginator.get_page(page_number)
        context["page_obj"] = paginator.get_page(page_number)
        return context


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

class AttachmentsCreate(CreateView):
    form_class = AttachmentsForm
    template_name = "task_attachments.html"
    success_url = reverse_lazy("attachments")
    context_object_name = "attachments"

# Сохранение файла из внешнего пути

# def save_attachments(file_path, task_id=4):
#     path = Path("/Users/tatya/OneDrive/Рабочий стол/FFF.txt")
#     task = Tasks.objects.get(id=task_id)
#     attachment = Attachments(
#         task=task,
#         name=path.name
#     )
#     with path.open(mode="rb") as f:
#         attachment.file = File(
#             f,
#             name=path.name
#         )
#         attachment.save()
#     return attachment
