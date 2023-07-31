# Generated by Django 4.1.4 on 2023-07-30 03:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="my_user",
            name="available_time",
        ),
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time",
                    models.CharField(
                        choices=[
                            ("time1", "Time1"),
                            ("time2", "Time2"),
                            ("time3", "Time3"),
                            ("time4", "Time4"),
                        ],
                        max_length=10,
                    ),
                ),
                ("date", models.DateField()),
                ("my_user", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
