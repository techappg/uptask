# Generated by Django 3.2.7 on 2022-02-16 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0028_auto_20220216_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='attendence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskapp.attendence'),
        ),
    ]