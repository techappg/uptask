# Generated by Django 3.2.7 on 2021-09-09 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0006_rename_domain_name_user_programming_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-id']},
        ),
    ]
