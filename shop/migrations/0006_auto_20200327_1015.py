# Generated by Django 3.0.3 on 2020-03-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]