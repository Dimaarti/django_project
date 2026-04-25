from django import forms

from task_manager.models import Tasks

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _





class CommentForm(forms.Form):
    message = forms.CharField(
        label="Комментарий",
        widget=forms.Textarea(
            attrs={"class": "form-control-lg"}
        )
    )
    user = forms.CharField(
        label="Пользователь",
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control-sm"}
        )
    )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["name", "description", "priority", "status"]
        widgets = {
            "description": forms.Textarea(
                attrs={'style': 'width:300px'}
            ),
        }

    def validator_priority(self):
        cleaned_data = super().clean()

        priority = cleaned_data.get("priority")
        description = cleaned_data.get("description")

        if priority == 5 is not description:
            raise forms.ValidationError("Приоритет без описания не может быть высоким")
        return cleaned_data