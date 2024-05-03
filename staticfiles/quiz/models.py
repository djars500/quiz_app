import django_summernote.fields
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from user.models import User


class Course(models.Model):
    name = models.CharField(verbose_name='Категория курса', max_length=255)
    description = models.TextField(verbose_name='Описание категории', null=True, blank=True)
    text = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Quiz(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тест')
    description = models.TextField(verbose_name='Описание')
    drag_drop = models.BooleanField(default=False, verbose_name='Перестаскивыемые вопросы')
    photo = models.FileField(upload_to='cource-photo', null=True, blank=True, verbose_name='Фото описание курса')
    file = models.FileField(upload_to='content/', null=True, blank=True, verbose_name='Тема для изучения')
    level = models.PositiveIntegerField(default=1, verbose_name='Уровень процента')
    category = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizes', verbose_name='Категория',
                                 null=True, blank=True)

    def get_finished_results(self):
        return self.quizresult.filter(finished=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема курса'
        verbose_name_plural = 'Темы курса'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    description = models.TextField(blank=True, null=True, verbose_name='Детальное описание')
    question_text = models.CharField(verbose_name='Текст вопроса', max_length=200, null=True, blank=True)
    file = models.FileField(verbose_name="Файл", upload_to='question/', null=True, blank=True)

    def __str__(self):
        return self.question_text if self.question_text != "" else self.id

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def get_answers(self):
        return self.choice.all().order_by('?')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice')
    text = models.CharField(max_length=200, verbose_name='Текст ответа', null=True, blank=True)
    file = models.FileField(verbose_name="Файл", upload_to='answer/', null=True, blank=True)
    is_correct = models.BooleanField(default=False, verbose_name='Правильный ответ')

    def __str__(self):
        if self.is_correct:
            return f"{self.question} - {self.text}"
        return f"{self.text}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizresult")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="quizresult")
    score = models.IntegerField()
    finished = models.BooleanField(default=False, verbose_name='Успешно пройден')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.score}"

    class Meta:
        verbose_name = 'Результаты теста'
        verbose_name_plural = 'Результаты теста'


class UserAnswer(models.Model):
    quiz_result = models.ForeignKey(QuizResult, on_delete=models.CASCADE, related_name='user_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_answer')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='user_answer')

    def __str__(self):
        return f"{self.quiz_result}"

    class Meta:
        verbose_name = 'Выбранные ответы теста'
        verbose_name_plural = 'Выбранные ответы теста'
