# Generated by Django 4.1.2 on 2022-10-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasine', '0023_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
