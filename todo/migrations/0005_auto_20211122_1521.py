# Generated by Django 3.2.9 on 2021-11-22 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_task_order_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='time',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='task',
            name='order_time',
        ),
    ]
