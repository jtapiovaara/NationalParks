# Generated by Django 3.1.3 on 2020-11-14 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('natparks', '0006_auto_20201114_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='natparks',
            old_name='ndescription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='natparks',
            old_name='nlocation',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='natparks',
            old_name='npicture',
            new_name='picture',
        ),
        migrations.RenameField(
            model_name='natparks',
            old_name='ntitle',
            new_name='title',
        ),
    ]
