# Generated by Django 3.0.4 on 2020-05-02 07:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('natparks', '0003_auto_20200502_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='natparkgeo',
            name='calltitle',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
