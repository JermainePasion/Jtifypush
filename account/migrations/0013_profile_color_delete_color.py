# Generated by Django 5.0.1 on 2024-02-10 12:26

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None),
        ),
        migrations.DeleteModel(
            name='color',
        ),
    ]
