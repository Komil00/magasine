# Generated by Django 4.1.2 on 2022-10-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasine', '0019_remove_orderproduct_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
