# Generated by Django 5.2 on 2025-06-12 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='vale',
        ),
        migrations.AddField(
            model_name='message',
            name='value',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=255),
        ),
    ]
