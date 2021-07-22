from django.db import models
from django.forms import ModelForm
from django.utils import timezone
# Create your models here.
from django import forms


class Todo(models.Model):
    title = models.CharField(max_length=50)
    contents = models.CharField(max_length=200)
    todo_date = models.DateTimeField('date',  auto_now=True)

    def __str__(self):
        return self.title


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'contents']

