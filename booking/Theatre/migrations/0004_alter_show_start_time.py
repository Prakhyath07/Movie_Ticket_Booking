# Generated by Django 4.1.6 on 2023-02-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Theatre", "0003_alter_movies_duration_alter_movies_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="show", name="start_time", field=models.DateTimeField(),
        ),
    ]