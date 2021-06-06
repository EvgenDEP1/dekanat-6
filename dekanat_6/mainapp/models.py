from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name='Группа', max_length=64)
    desc = models.TextField(verbose_name='Специальность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Student(models.Model):
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.CASCADE)
    surname = models.CharField(verbose_name='Фамилия', max_length=64)
    name = models.CharField(verbose_name='Имя', max_length=64)
    patronymic = models.CharField(verbose_name='Отчество', max_length=64, blank=True)

    def __str__(self):
        return f'{self.surname} | {self.group}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        # ordering = ['-created']
