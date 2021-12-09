# Generated by Django 3.2.9 on 2021-12-05 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_task_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Category',
        ),
        migrations.AddField(
            model_name='task',
            name='Category',
            field=models.ManyToManyField(related_name='category_task', related_query_name='cat_task', to='todo.Category'),
        ),
    ]
