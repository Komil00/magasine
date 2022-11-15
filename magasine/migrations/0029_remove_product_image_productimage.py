# Generated by Django 4.1.2 on 2022-11-14 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magasine', '0028_alter_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magasine.product')),
            ],
        ),
    ]
