# Generated by Django 3.2.7 on 2022-02-03 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0030_attendence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='attend_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
