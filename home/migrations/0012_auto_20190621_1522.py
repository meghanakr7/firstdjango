# Generated by Django 2.2.2 on 2019-06-21 09:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20190621_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Borrowed_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 21, 9, 52, 15, 170438, tzinfo=utc)),
        ),
    ]