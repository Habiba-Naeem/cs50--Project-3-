# Generated by Django 2.2.10 on 2020-06-05 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20200605_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='additional',
            new_name='additionals',
        ),
    ]