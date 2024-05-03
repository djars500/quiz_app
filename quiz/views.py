from random import shuffle
from django.contrib import messages
from django import template
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from quiz.models import Quiz, Question, QuizResult, UserAnswer, Answer, Course

register = template.Library()


@login_required(login_url='/user/auth/')
def take_quiz(request, *args, **kwargs):
    quiz = Quiz.objects.get(id=kwargs['pk'])
    paginator = Paginator(quiz.questions.all(), 10)
    page = request.GET.get('page', 1)
    paged_items = paginator.get_page(page)
    questions = list(quiz.questions.all())
    shuffle(questions)
    context = {
        "quiz": quiz,
        "questions": questions,
        "paged_items": paged_items,
        "objs": questions
    }
    return render(request, 'quiz/app-take-quiz.jinja2', context)

@login_required(login_url='/user/auth/')
def take_quiz(request, *args, **kwargs):
    quiz = Quiz.objects.get(id=kwargs['pk'])
    paginator = Paginator(quiz.questions.all(), 10)
    page = request.GET.get('page', 1)
    paged_items = paginator.get_page(page)
    questions = list(quiz.questions.all())
    shuffle(questions)
    context = {
        "quiz": quiz,
        "questions": questions,
        "paged_items": paged_items,
        "objs": questions
    }
    return render(request, 'quiz/app-take-quiz.jinja2', context)


@login_required(login_url='/user/auth/')
def send_quiz(request, *args, **kwargs):
    data = dict(request.POST)
    data.pop('csrfmiddlewaretoken')
    answers = []
    score = 0
    result = QuizResult.objects.create(user=request.user,
                                       quiz_id=kwargs['pk'],
                                       score=score
                                       )

    for key, value in data.items():
        question = Question.objects.get(id=key)

        for answer in value:
            try:
                choice = question.choice.get(id=answer)
                if choice.is_correct:
                    score += 1
            except Answer.DoesNotExist:
                choice = Answer.objects.get(id=answer)

            answers.append(UserAnswer(
                question_id=question.id,
                answer_id=choice.id,
                quiz_result=result
            ))
    quiz = Quiz.objects.get(id=kwargs['pk'])

    count_of_questions = quiz.questions.count()
    score_percent = score * 100 / count_of_questions
    if score_percent >= quiz.level:
        result.finished = True
        messages.success(request, 'Тест успешно пройден')
    else:
        messages.warning(request, 'Вы не смогли сдать тест')
    result.score = score_percent
    result.save()
    UserAnswer.objects.bulk_create(answers)

    return JsonResponse(data={
        'path': reverse('start-course', args=[quiz.category.id])
    })


@login_required(login_url='/user/auth/')
def cources(request):
    quizes = Course.objects.all()
    return render(request, 'cources/app-student-courses.jinja2', {"quizes": quizes})

@login_required(login_url='/user/auth/')
def start_quiz(request, *args, **kwargs):
    course = Course.objects.get(id=kwargs['pk'])
    quizes = course.quizes.all().order_by('level')
    context = {
        'quizes': quizes,
        'course': course
    }
    return render(request, 'cources/app-take-course.jinja2', context)

@login_required(login_url='/user/auth/')
def get_course(request, *args, **kwargs):
    category = Course.objects.get(id=kwargs['pk'])
    quizes = category.quizes.all().order_by('level')
    total_score = 0
    count_quiz = 0
    for quiz in quizes:
        if quiz.quizresult.order_by('score').count() > 0:
            score = getattr(quiz.quizresult.order_by('score').last(), 'score', 0)
            total_score += score
            count_quiz += 1

    context = {
        'quizes': quizes,
        'category': category,
        'count_quiz': count_quiz,
    }
    return render(request, 'cources/app-student-course.jinja2', context)
