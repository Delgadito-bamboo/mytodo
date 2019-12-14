# Generated by Django 2.2 on 2019-12-07 06:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('tag', models.ManyToManyField(to='todo.Tag')),
            ],
        ),
    ]