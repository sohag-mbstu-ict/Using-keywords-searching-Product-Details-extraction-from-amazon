# Generated by Django 4.2.1 on 2023-05-07 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('First_bot', '0007_alter_product_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
    ]
