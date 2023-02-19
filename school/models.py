from django.db import models
from django.contrib.auth import get_user_model

days = (
    ('Понедельник', 'Понедельник'),
    ('Вторник', 'Вторник'),
    ('Среда', 'Среда'),
    ('Четверг', 'Четверг'),
    ('Пятница', 'Пятница'),
    ('Суббота', 'Суббота'),
    ('Воскресенье', 'Воскресенье'),
)

class News(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()
    image = models.ImageField(upload_to='news_images/', blank=True)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()

    def get_about_text(self):
        return f'{self.text[:100]}...'.strip()

    def __str__(self):
        return self.title


class Subject(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='teachers_photo/', blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=True)
    role = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()
    cabinet = models.CharField(max_length=10)
    phone = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_query_name='subject')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_query_name='user', related_name='enrollments')
    date = models.DateField(auto_now_add=True, null=True)
    accepted = models.BooleanField(default=False, verbose_name='Принят')

    def __str__(self):
        return self.user.username


class Lesson(models.Model):
    day = models.CharField(max_length=11, choices=days)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=5)
    end_time = models.CharField(max_length=5)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    cabinet = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.subject)
