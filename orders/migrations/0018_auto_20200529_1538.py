# Generated by Django 2.2.10 on 2020-05-29 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20200528_2149'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubsItems',
            new_name='Subs_Items',
        ),
        migrations.RenameField(
            model_name='subs',
            old_name='sub',
            new_name='subs_items',
        ),
    ]
