from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('group/', mainapp.group, name='group'),
    path('group/show/<int:pk>/', mainapp.group_show, name='group_show'),
    path('group/create/', mainapp.group_create, name='group_create'),
    path('group/delete/<int:pk>/', mainapp.group_delete, name='group_delete'),
    path('group/change/<int:pk>/', mainapp.group_change, name='group_change'),

    path('group/show/student_create/', mainapp.student_create, name='student_create'),
    path('group/show/student_delete/<int:pk>/', mainapp.student_delete, name='student_delete'),
    path('group/show/student_change/<int:pk>/', mainapp.student_change, name='student_change'),
]
