# Generated by Django 4.2.6 on 2023-10-24 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='dep_description',
            new_name='dep_decription',
        ),
    ]
