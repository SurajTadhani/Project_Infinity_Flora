# Generated by Django 5.0.6 on 2024-05-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0010_remove_homeclients_headimg7'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100, null=True)),
                ('headContent1', models.TextField(max_length=1000, null=True)),
                ('headContent2', models.TextField(max_length=1000, null=True)),
                ('headContent3', models.TextField(max_length=1000, null=True)),
                ('headContent4', models.TextField(max_length=1000, null=True)),
                ('headImg', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]