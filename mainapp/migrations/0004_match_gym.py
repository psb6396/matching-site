# Generated by Django 4.1.4 on 2023-08-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_remove_match_my_user_match_player_match_referee_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="match",
            name="gym",
            field=models.CharField(max_length=50, null=True),
        ),
    ]