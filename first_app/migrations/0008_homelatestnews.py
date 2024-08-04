# Generated by Django 5.0.6 on 2024-05-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_alter_homeslider_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='homelatestnews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headImg', models.ImageField(upload_to='images/')),
                ('header', models.CharField(max_length=100, null=True)),
                ('date', models.CharField(max_length=100, null=True)),
                ('paragraph', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
