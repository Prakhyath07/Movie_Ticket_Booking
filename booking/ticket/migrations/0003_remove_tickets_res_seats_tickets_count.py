# Generated by Django 4.1.6 on 2023-02-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticket", "0002_tickets_res_seats"),
    ]

    operations = [
        migrations.RemoveField(model_name="tickets", name="res_seats",),
        migrations.AddField(
            model_name="tickets",
            name="count",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
