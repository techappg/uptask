# Generated by Django 3.2.7 on 2021-12-29 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0011_multiple_select_language_multiple_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiple_select_language',
            name='multiple_language',
        ),
    ]
