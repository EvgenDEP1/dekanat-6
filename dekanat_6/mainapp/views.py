from django.shortcuts import render
from mainapp.models import Group
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from forms import GroupForm

def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


def group(request):
    group = Group.objects.all()
    context = {
        'title': 'группы',
        'groups': group,
    }
    return render(request, 'mainapp/group.html', context)


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Группа добавлена успешно')
            return HttpResponseRedirect(reverse('mainapp:group'))
    else:
        form = GroupForm()
    context = {
        'title': 'Добавить группу',
        'form': form,
    }
    return render(request, 'mainapp/group_add.html', context)
