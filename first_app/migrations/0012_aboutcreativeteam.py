# Generated by Django 5.0.6 on 2024-05-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0011_aboutinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutcreativeteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamsImg', models.ImageField(null=True, upload_to='images/')),
                ('heading', models.CharField(max_length=100, null=True)),
                ('paragraph', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
