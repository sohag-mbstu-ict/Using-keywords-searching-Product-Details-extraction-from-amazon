# Generated by Django 4.2.1 on 2023-05-08 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_bot', '0011_productdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdescription',
            name='total_rating',
            field=models.IntegerField(default=0),
        ),
    ]
