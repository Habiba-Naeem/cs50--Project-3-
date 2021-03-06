# Generated by Django 2.2.10 on 2020-06-04 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_menu'),
        ('cart', '0004_auto_20200602_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='extra_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='extras',
        ),
        migrations.RemoveField(
            model_name='product',
            name='toppings',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Extra')),
                ('toppings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Toppings')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='additional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.Additional'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.Category'),
        ),
    ]
