# Generated by Django 2.2.3 on 2019-08-06 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bed',
            name='title',
        ),
    ]
