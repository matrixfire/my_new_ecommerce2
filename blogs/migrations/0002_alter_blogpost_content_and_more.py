# Generated by Django 4.0 on 2023-12-14 10:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='description_html',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
