# Generated by Django 4.0 on 2021-12-14 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('grade', models.CharField(choices=[('Elementry', 'Elementry'), ('Middle', 'Middle'), ('High', 'High')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('courses', models.CharField(choices=[('English', 'English'), ('Math', 'Math'), ('Physics', 'Physics'), ('Science', 'Science')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
