# Generated by Django 2.2.10 on 2020-05-14 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_remove_subs_items_sub_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platter_item',
            name='size',
        ),
        migrations.RemoveField(
            model_name='subs_items',
            name='size',
        ),
        migrations.AddField(
            model_name='dinnerplatters',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
        migrations.AddField(
            model_name='subs',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Size'),
        ),
    ]
