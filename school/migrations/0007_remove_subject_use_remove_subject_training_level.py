# Generated by Django 4.1.7 on 2023-02-19 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_teacher_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='USE',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='training_level',
        ),
    ]
