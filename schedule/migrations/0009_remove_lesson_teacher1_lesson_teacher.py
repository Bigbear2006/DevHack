# Generated by Django 4.1.7 on 2023-02-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_remove_lesson_teacher_lesson_teacher1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='teacher1',
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
