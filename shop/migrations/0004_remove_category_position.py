# Generated by Django 3.0.3 on 2020-03-26 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200327_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='position',
        ),
    ]
