# Generated by Django 4.2 on 2023-04-28 05:33

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_course_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Text'),
        ),
    ]