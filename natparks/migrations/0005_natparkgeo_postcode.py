# Generated by Django 3.1.3 on 2020-11-14 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natparks', '0004_natparkgeo_calltitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='natparkgeo',
            name='postcode',
            field=models.IntegerField(blank=True, default=99999),
        ),
    ]
