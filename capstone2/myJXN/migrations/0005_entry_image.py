# Generated by Django 4.1.2 on 2022-10-28 02:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myJXN', '0004_rename_location_entry_lat_entry_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
    ]
