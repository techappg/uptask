# Generated by Django 3.2.7 on 2022-02-01 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0025_attendence'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='puch_in',
            new_name='punch_in',
        ),
    ]
