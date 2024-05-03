from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Sum, F, Count, Avg, Max, Min
from django.shortcuts import render, redirect, reverse

from quiz.models import Course, QuizResult, Quiz
from user.forms import CustomAuthenticationForm, CustomRegistrationForm
from user.models import DocFilesUser, User


@login_required(login_url='auth')
def main(request, *args, **kwargs):
    courses = Course.objects.values("id", "name", quiz_count=Count('quizes')).filter(
        quizes__quizresult__finished=True).annotate(
        sum_result=Sum("quizes__quizresult__score") / F('quiz_count'))[:3]
    course_count = Course.objects.count()
    quizes = QuizResult.objects.filter(finished=True, user=request.user)
    test_result = quizes.aggregate(amount=Sum('score', default=0))['amount'] / quizes.count()
    sertificates = DocFilesUser.objects.filter(user=request.user)
    diagram = {
        "age": User.objects.aggregate(avg_age=Avg('age', default=0), max_age=Max('age', default=0),
                                      min_age=Min('age', default=0)),
        "gender_m": User.objects.filter(gender=1).count(),
        "gender_w": User.objects.filter(gender=2).count(),
        "score": QuizResult.objects.aggregate(max_score=Max('score', default=0),
                                              avg_score=Avg('score', default=0))
    }
    circle = Quiz.objects.all()
    context = {
        'courses': courses,
        'course_count': course_count,
        'test_result': int(test_result),
        'sertificates': sertificates,
        'diagram': diagram

    }
    # return render(request, 'base/base.jinja2')
    return render(request, 'user/dashboard.jinja2', context)


def register_view(request):
    with transaction.atomic():
        if request.method == 'POST':
            form = CustomRegistrationForm(data=request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.pop('password')
                user = User.objects.create(**form.cleaned_data)
                user.set_password(password)
                login(request, user)
                return redirect(reverse('dashboard'))
        else:
            form = CustomRegistrationForm()
        return render(request, 'user/sign-up.jinja2', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('dashboard'))
    else:
        form = CustomAuthenticationForm()
    return render(request, 'user/auth_user.jinja2', {'form': form})


def profile_view(request):
    return render(request, 'user/app-student-profile.jinja2', {})
