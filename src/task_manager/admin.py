from django.contrib import admin
from django.contrib.admin import TabularInline
from django.db.models import QuerySet
from django.utils.safestring import mark_safe

from task_manager.models import Tasks, Tags, Projects, ProjectsDetails, Comments, Attachments


class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 2


class AttachmentsTabularInline(admin.TabularInline):
    model = Attachments


class AttachmentsStackedInline(admin.StackedInline):
    model = Attachments


class ProjectsdetailsInline(admin.StackedInline):
    model = ProjectsDetails


class TagsInline(admin.StackedInline):
    model = Tags.tasks.through


class AssigneeFilter(admin.SimpleListFilter):
    title = "Фильтр по исполнителю"
    parameter_name = "assignee_filter"

    def lookups(self, request, model_admin):
        return [
            ("yes", "Без исполнителя"),
            ("no", "С исполнителем"),
            ("", "Пустое значение")
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == "yes":
            return queryset.filter(assignee__isnull=True)
        if self.value() == "no":
            return queryset.filter(assignee__isnull=False)
        return queryset


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    fields = [("name", "status"), "description", "priority", "project", "comments_count", "created_at", "is_reopened"]
    list_display = ["name", "status", "priority", "assignee_email"]
    list_display_links = ["name", "status"]
    list_editable = ["priority"]
    readonly_fields = ["created_at", "comments_count"]
    inlines = [AttachmentsStackedInline, CommentsInline, AttachmentsTabularInline, TagsInline]
    list_filter = ["priority", "status", "project", AssigneeFilter]
    actions = ["status_completed", "status_canceled", "reopened", "create_comment"]

    @admin.display(description="assignee email", ordering="assignee_email")
    def assignee_email(self, obj):
        return obj.assignee.email if obj.assignee else None

    @admin.display(description="comments")
    def comments_count(self, obj):
        count_comments = Comments.objects.filter(task=obj).count()
        return mark_safe(f"<h1>{count_comments}</h1>")

    @admin.action(description="Mark selected status tasks as Completed")
    def status_completed(self, request, queryset):
        queryset.update(status="completed")

    @admin.action(description="Mark selected status tasks as Canceled")
    def status_canceled(self, request, queryset):
        queryset.update(status="canceled")

    @admin.action(description="Resetting the reopening flag")
    def reopened(self, request, queryset):
        queryset.update(is_reopened=False)

    # @admin.action(description="Create comment")
    # def create_comment(self, request, queryset):
    #     for task in queryset:
    #         Comments.objects.create(task=task, message="Processed by admin")


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    fields = ["name", "description"]
    exclude = ["owner"]
    inlines = [ProjectsdetailsInline]


@admin.register(ProjectsDetails)
class ProjectsDetailsAdmin(admin.ModelAdmin):
    pass


class CommentsAdmin(admin.ModelAdmin):
    pass


class AttachmentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comments, CommentsAdmin)
admin.site.register(Attachments, AttachmentsAdmin)
# Register your models here.
