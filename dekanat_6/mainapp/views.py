from django.shortcuts import render
from mainapp.models import Group

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
