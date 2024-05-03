from email.policy import default

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    type_gender = (
        (1, 'Мальчик'),
        (2, 'Девочка')
    )

    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(verbose_name='email address', unique=True)
    gender = models.IntegerField(choices=type_gender, default=1)
    phone = models.CharField(max_length=11)
    photo = models.ImageField(upload_to="users/", null=True, blank=True)
    age = models.IntegerField(default=18)
    ent_result = models.IntegerField(verbose_name='Результат ент', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class DocFilesUser(models.Model):
    file = models.FileField(verbose_name='Файлы')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
