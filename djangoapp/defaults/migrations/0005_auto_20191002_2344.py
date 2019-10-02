# Generated by Django 2.2.5 on 2019-10-02 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defaults', '0004_auto_20191002_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('green', 'Green'), ('black', 'Black')], max_length=6),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 2, 23, 44, 24, 38409)),
        ),
    ]
