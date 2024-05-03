# Generated by Django 4.2 on 2023-04-28 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_course_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Тема курса', 'verbose_name_plural': 'Темы курса'},
        ),
        migrations.AlterModelOptions(
            name='useranswer',
            options={'verbose_name': 'Выбранные ответы теста', 'verbose_name_plural': 'Выбранные ответы теста'},
        ),
        migrations.AddField(
            model_name='course',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
