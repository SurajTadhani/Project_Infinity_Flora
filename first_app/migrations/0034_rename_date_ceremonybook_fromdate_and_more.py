# Generated by Django 5.0.6 on 2024-07-08 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0033_items_details_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ceremonybook',
            old_name='date',
            new_name='fromDate',
        ),
        migrations.AddField(
            model_name='ceremonybook',
            name='toDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
