# Generated by Django 4.1.2 on 2022-10-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasine', '0013_alter_orderproduct_author_alter_orderproduct_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]