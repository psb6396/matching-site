# Generated by Django 4.0.4 on 2024-02-06 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gym',
            name='adress',
        ),
    ]
