# Generated by Django 4.2.7 on 2024-05-01 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_on_get',
        ),
        migrations.RemoveField(
            model_name='order',
            name='requires_delivery',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='land_area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Площадь земли (в кв. м)'),
        ),
        migrations.AddField(
            model_name='order',
            name='land_processing_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата обработки земли'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(blank=True, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата сделки'),
        ),
    ]
