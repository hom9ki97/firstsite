from django import forms
from .models import CodeExample, Lessons, HomeWork, Topic


class CodeExampleForm(forms.ModelForm):
    class Meta:
        model = CodeExample
        fields = ['lesson', 'homework', 'code_file', 'description']


class LessonsForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ['title', 'order', 'content', 'topic']


class HomeWorkForm(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = ['lesson', 'task', 'order']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'description', 'language']
