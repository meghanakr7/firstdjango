# Generated by Django 2.2.2 on 2019-06-21 04:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190620_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Borrowed_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 21, 9, 57, 11, 909413)),
        ),
    ]
