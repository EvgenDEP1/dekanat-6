# from django import forms
from django.forms import ModelForm

from mainapp.models import Group, Student


class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ('name', 'desc')


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ('group', 'surname', 'name', 'patronymic')
