# Generated by Django 4.1.3 on 2022-11-06 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0023_alter_album_creation_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creation_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 6, 9, 40, 48, 759683)),
        ),
    ]
