# Generated by Django 3.0.3 on 2020-03-26 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200327_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.Category'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Category'),
        ),
    ]