# Generated by Django 3.2.7 on 2021-12-14 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_delete_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='added_on',
        ),
    ]
