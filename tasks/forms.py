from django import forms

from tasks.models import TasksDB


class ContentForm(forms.ModelForm):
    class Meta:
        model = TasksDB
        fields = ('content', )
