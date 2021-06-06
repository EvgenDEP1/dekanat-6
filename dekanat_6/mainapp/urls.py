from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('group/', mainapp.group, name='group'),
    path('group/show/<int:pk>/', mainapp.group_show, name='group_show'),
    path('group/create/', mainapp.group_create, name='group_create'),
    path('user/group/delete/<int:pk>/', mainapp.group_delete, name='group_delete'),
    path('group/change/<int:pk>/', mainapp.group_change, name='group_change'),
]
