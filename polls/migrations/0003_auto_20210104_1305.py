# Generated by Django 3.1.4 on 2021-01-04 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210104_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='description',
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.CharField(default='Brief description', max_length=500),
        ),
    ]
