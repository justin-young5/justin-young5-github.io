# Generated by Django 4.1.2 on 2022-10-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myJXN', '0009_alter_entry_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='name',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
