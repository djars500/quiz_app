import django_summernote.admin
from django.contrib import admin

from quiz.models import Quiz, Question, Course, Answer, QuizResult, UserAnswer


class QuestionInline(admin.TabularInline):
    model = Question


class ChoiceInline(admin.TabularInline):
    model = Answer


class QuizInline(admin.TabularInline):
    model = Quiz


class UserAnswerInline(admin.TabularInline):
    model = UserAnswer
    readonly_fields = ('question', 'answer', 'correct_answer')

    @staticmethod
    def correct_answer(obj):
        if obj.question == obj.answer.question and obj.answer.is_correct:
            return True
        return False


@admin.register(Course)
class CourseAdmin(django_summernote.admin.SummernoteModelAdmin):
    list_display = ('id', 'name')
    inlines = [
        QuizInline,
    ]

    summernote_fields = ('body',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'level',)
    list_filter = ('category', 'level',)
    inlines = [
        QuestionInline,
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'quiz',)
    list_filter = ('quiz', 'quiz__category')
    inlines = [
        ChoiceInline,
    ]


@admin.register(Answer)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'text', 'is_correct')
    list_filter = ('question', 'is_correct', 'question__quiz')


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'quiz_result', 'question', 'answer', 'is_correct_answer')
    list_filter = ('quiz_result',)

    @staticmethod
    def is_correct_answer(obj):
        return bool(obj.answer.is_correct)

    is_correct_answer.boolean = True


@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'quiz', 'date', 'user', 'finished')
    list_filter = ('user', 'quiz', 'finished')
    inlines = [
        UserAnswerInline
    ]


admin.site.register(UserAnswer, UserAnswerAdmin)
