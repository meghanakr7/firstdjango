# Generated by Django 2.2.2 on 2019-06-20 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190620_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='total_book_written',
            field=models.TextField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], null=True),
        ),
    ]
