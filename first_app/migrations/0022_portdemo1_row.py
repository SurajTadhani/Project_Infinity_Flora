# Generated by Django 5.0.6 on 2024-05-21 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0021_portdemo1'),
    ]

    operations = [
        migrations.AddField(
            model_name='portdemo1',
            name='row',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
