# Generated by Django 4.1.2 on 2022-10-17 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magasine', '0008_alter_product_category_alter_product_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='userfavoriteproduct',
            old_name='user',
            new_name='author',
        ),
    ]
