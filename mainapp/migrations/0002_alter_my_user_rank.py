# Generated by Django 4.1.4 on 2024-01-08 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="my_user",
            name="rank",
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]