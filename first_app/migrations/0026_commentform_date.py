# Generated by Django 5.0.6 on 2024-06-14 06:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0025_commentform'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentform',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
