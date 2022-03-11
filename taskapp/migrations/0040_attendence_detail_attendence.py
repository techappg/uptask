# Generated by Django 3.2.7 on 2022-03-09 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0039_auto_20220309_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attend_date', models.DateField(auto_now_add=True)),
                ('presence', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Detail_attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punch_in', models.TimeField(blank=True, null=True)),
                ('punch_out', models.TimeField(blank=True, null=True)),
                ('attend_date', models.DateField(auto_now_add=True, null=True)),
                ('working_hours', models.CharField(blank=True, max_length=30, null=True)),
                ('attendence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskapp.attendence')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskapp.user')),
            ],
        ),
    ]