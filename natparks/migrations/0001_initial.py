# Generated by Django 3.0.4 on 2020-03-14 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NatParks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('location', models.URLField(blank=True)),
            ],
        ),
    ]
