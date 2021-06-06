# from django import forms
from django.forms import ModelForm

from mainapp.models import Group


class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ('name', 'desc')
