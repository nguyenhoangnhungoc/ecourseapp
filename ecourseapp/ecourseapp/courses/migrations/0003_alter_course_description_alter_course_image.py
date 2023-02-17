# Generated by Django 4.1.7 on 2023-02-17 11:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='courses/static/%Y/%m'),
        ),
    ]