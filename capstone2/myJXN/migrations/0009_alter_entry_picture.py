# Generated by Django 4.1.2 on 2022-10-28 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myJXN', '0008_alter_entry_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
