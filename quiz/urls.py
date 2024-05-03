from django.urls import path

from quiz.views import take_quiz, send_quiz, cources, start_quiz, get_course

urlpatterns = [
    path('courses/', cources, name='courses'),
    path('course/<int:pk>/', get_course, name='course'),
    path('course/<int:pk>/start/', start_quiz, name='start-course'),
    path('take-quiz/start/', take_quiz, name='start-quiz'),
    path('take-quiz/<int:pk>/start/', take_quiz, name='start-quiz'),
    path('take-quiz/<int:pk>/start/save/', send_quiz, name='send-quiz'),
]
