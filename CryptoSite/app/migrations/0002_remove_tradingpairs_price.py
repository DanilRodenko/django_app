# Generated by Django 4.0.4 on 2022-06-23 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradingpairs',
            name='price',
        ),
    ]
