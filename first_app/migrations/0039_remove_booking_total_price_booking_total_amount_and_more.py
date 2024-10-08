# Generated by Django 5.0.6 on 2024-07-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0038_alter_booking_amount_alter_booking_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='total_price',
        ),
        migrations.AddField(
            model_name='booking',
            name='total_amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
