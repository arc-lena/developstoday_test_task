# Generated by Django 3.1.5 on 2021-01-06 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="creation_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="post",
            name="creation_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
