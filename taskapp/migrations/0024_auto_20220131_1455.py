# Generated by Django 3.2.7 on 2022-01-31 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0023_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigned_system_detail',
            name='assigned_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='assigned_system_detail',
            name='returned_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]
