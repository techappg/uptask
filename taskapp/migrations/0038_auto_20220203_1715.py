# Generated by Django 3.2.7 on 2022-02-03 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0037_alter_attendence_punch_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='attend_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='punch_in',
            field=models.TimeField(default=''),
        ),
    ]
