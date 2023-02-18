from django.db import models
from django.contrib.auth import get_user_model


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


class Teacher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='teachers_photo/', blank=True)
    slug = models.SlugField(null=True)
    role = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()
    cabinet = models.CharField(max_length=10)
    phone = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    description = models.TextField()
    training_level = models.CharField(max_length=100)
    USE = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_query_name='subject')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_query_name='user')
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

