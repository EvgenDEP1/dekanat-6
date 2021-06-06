from django.shortcuts import render, get_object_or_404
from mainapp.models import Group, Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from mainapp.forms import GroupForm, StudentForm


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


def group(request):
    groups = Group.objects.all()
    context = {
        'title': 'группы',
        'groups': groups,
    }
    return render(request, 'mainapp/group.html', context)


def group_show(request, pk):
    group_viewing = get_object_or_404(Group, pk=pk)
    students = Student.objects.filter(group=group_viewing)

    context = {
        'page_title': 'Группа',
        'students': students,
    }

    return render(request, 'mainapp/group_show.html', context)


def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:group'))
    else:
        form = GroupForm()
    context = {
        'title': 'Добавить группу',
        'form': form,
    }
    return render(request, 'mainapp/group_create.html', context)


def group_delete(request, pk):
    group = Group.objects.get(pk=pk)
    group.delete()
    return HttpResponseRedirect(reverse('mainapp:group'))


def group_change(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:group'))
    else:
        form = GroupForm(instance=group)
    context = {
        'title': 'Изменить группу',
        'form': form,
    }
    return render(request, 'mainapp/group_create.html', context)

