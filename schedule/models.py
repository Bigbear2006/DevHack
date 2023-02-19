from django.db import models
from school.models import Teacher, Subject

days = (
    ('Понедельник', 'Понедельник'),
    ('Вторник', 'Вторник'),
    ('Среда', 'Среда'),
    ('Четверг', 'Четверг'),
    ('Пятница', 'Пятница'),
    ('Суббота', 'Суббота'),
    ('Воскресенье', 'Воскресенье'),
)


class Faculty(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название факультета')

    def __str__(self):
        return self.name


class Course(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name='Факультет')
    number = models.PositiveIntegerField(verbose_name='Номер курса')

    def __str__(self):
        return f'{self.number}'


class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1, verbose_name='Курс')
    name = models.CharField(max_length=255, verbose_name='Название группы')

    def __str__(self):
        return str(self.name)


class Lesson(models.Model):
    day = models.CharField(max_length=11, choices=days)
    start_time = models.CharField(max_length=5)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    end_time = models.CharField(max_length=5)
    name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    cabinet = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.name)
