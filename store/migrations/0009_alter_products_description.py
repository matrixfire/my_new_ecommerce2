# Generated by Django 4.0 on 2023-11-29 15:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_products_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
