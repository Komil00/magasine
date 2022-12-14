# Generated by Django 4.1.2 on 2022-10-18 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magasine', '0011_alter_product_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='author',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='magasine.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='magasine.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='modelname',
            field=models.CharField(blank=True, default=1, max_length=50),
            preserve_default=False,
        ),
    ]
