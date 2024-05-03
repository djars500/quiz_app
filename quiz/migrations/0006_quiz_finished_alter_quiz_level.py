# Generated by Django 4.2 on 2023-05-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_course_options_alter_quiz_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='Успешно пройден'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='level',
            field=models.PositiveIntegerField(default=1, verbose_name='Уровень процента'),
        ),
    ]