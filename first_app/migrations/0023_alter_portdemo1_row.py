# Generated by Django 5.0.6 on 2024-05-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0022_portdemo1_row'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portdemo1',
            name='row',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
