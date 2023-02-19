# Generated by Django 4.1.7 on 2023-02-18 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_teacher_subject'),
        ('schedule', '0007_alter_lesson_day_alter_lesson_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='teacher',
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.teacher'),
        ),
    ]
