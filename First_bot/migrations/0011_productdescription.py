# Generated by Django 4.2.1 on 2023-05-07 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('First_bot', '0010_delete_productdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=750)),
                ('availability', models.CharField(max_length=15)),
                ('rating', models.FloatField()),
                ('price', models.FloatField()),
                ('shipping_import_price', models.FloatField()),
                ('delivery', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=20)),
                ('connectivity_technology', models.CharField(max_length=20)),
                ('connector_type', models.CharField(max_length=30)),
                ('compatible_device', models.TextField(max_length=500)),
                ('compatible_models', models.TextField(max_length=700)),
                ('special_features', models.TextField(max_length=300)),
                ('color', models.CharField(max_length=15)),
                ('input_voltage', models.CharField(max_length=15)),
                ('mounting_type', models.CharField(max_length=50)),
                ('about_this_item', models.TextField(max_length=2000)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='First_bot.product')),
            ],
        ),
    ]