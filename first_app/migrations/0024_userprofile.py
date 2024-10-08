# Generated by Django 5.0.6 on 2024-05-21 09:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0023_alter_portdemo1_row'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('contact', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
