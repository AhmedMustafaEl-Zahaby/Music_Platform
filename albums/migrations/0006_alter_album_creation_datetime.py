# Generated by Django 4.1.3 on 2022-11-10 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_alter_album_creation_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creation_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 10, 17, 43, 40, 195090)),
        ),
    ]
