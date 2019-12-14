# Generated by Django 2.2 on 2019-12-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(blank=True, choices=[('uncompleted', '未完了'), ('completed', '完了')], max_length=10),
        ),
        migrations.AlterField(
            model_name='todo',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]