# Generated by Django 4.2.7 on 2024-05-01 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_alter_cart_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='session_key',
        ),
    ]