# Generated by Django 3.1.7 on 2021-03-17 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_des',
            new_name='task_description',
        ),
    ]
