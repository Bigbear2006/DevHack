from django.db import models

days = (
    ('1', 'Понедельник'),
    ('2', 'Вторник'),
    ('3', 'Среда'),
    ('4', 'Четверг'),
    ('5', 'Пятница'),
    ('6', 'Суббота'),
    ('7', 'Воскресенье'),
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
        return self.name


class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    day = models.CharField(max_length=11, choices=days)

    def __str__(self):
        return self.day


class Lesson(models.Model):
    start_time = models.CharField(max_length=5)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    end_time = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255)
    cabinet = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
