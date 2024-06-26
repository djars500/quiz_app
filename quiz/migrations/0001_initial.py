# Generated by Django 4.2 on 2023-04-28 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст ответа')),
                ('file', models.FileField(blank=True, null=True, upload_to='answer/', verbose_name='Файл')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Правильный ответ')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория курса')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Категория теста',
                'verbose_name_plural': 'Категории теста',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Детальное описание')),
                ('question_text', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст вопроса')),
                ('file', models.FileField(blank=True, null=True, upload_to='question/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Тест')),
                ('description', models.TextField(verbose_name='Описание')),
                ('drag_drop', models.BooleanField(default=False, verbose_name='Перестаскивыемые вопросы')),
                ('photo', models.FileField(blank=True, null=True, upload_to='cource-photo', verbose_name='Фото описание курса')),
                ('file', models.FileField(blank=True, null=True, upload_to='content/', verbose_name='Тема для изучения')),
                ('level', models.PositiveIntegerField(default=1, verbose_name='Уровень')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizes', to='quiz.course', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Результаты теста',
                'verbose_name_plural': 'Результаты теста',
            },
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to='quiz.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to='quiz.question')),
                ('quiz_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to='quiz.quizresult')),
            ],
            options={
                'verbose_name': 'Результаты ответов теста',
                'verbose_name_plural': 'Результаты ответов теста',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.quiz'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='quiz.question'),
        ),
    ]
