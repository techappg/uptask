# Generated by Django 3.2.7 on 2022-01-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0022_auto_20220124_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
