# Generated by Django 5.0.6 on 2024-06-14 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0024_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='commentform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('msg', models.TextField()),
            ],
        ),
    ]