# Generated by Django 4.1.2 on 2022-10-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasine', '0016_orderproduct_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
