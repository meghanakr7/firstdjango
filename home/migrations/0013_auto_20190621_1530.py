# Generated by Django 2.2.2 on 2019-06-21 10:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190621_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Borrowed_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 21, 10, 0, 1, 337417, tzinfo=utc)),
        ),
    ]
