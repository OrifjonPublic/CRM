from django.db import models
from django.contrib.auth.models import AbstractUser
from lesson.models import Lesson


def image_path(instance, filename):
    return f'{instance.first_name}/'


class User(AbstractUser):

    STATUS = (
        ('admin', 'ADMIN'),
        ('assist', 'ASSIST'),
        ('ustoz', 'USTOZ'),
        ('pupil', 'PUPIL'),
    )
    status = models.CharField(max_length=15, choices=STATUS, default='pupil', verbose_name='Foydalanuvchi turi')

    def __str__(self) -> str:
        return self.username


class Manager(models.Model):
    manager = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')
    phone_number = models.CharField(max_length=13, verbose_name='Telefon raqam ', null=True, blank=True)
    image = models.ImageField(upload_to='manager/', verbose_name='Foydalanuvchi rasmi ', null=True, blank=True)

    def __str__(self) -> str:
        return self.manager.username
        

class Administrator(models.Model):
    phone_number = models.CharField(max_length=13, verbose_name='Telefon raqam ', null=True, blank=True)
    administrator = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrator')
    image = models.ImageField(upload_to='administrator/', verbose_name='Foydalanuvchi rasmi ', null=True, blank=True)

    def __str__(self) -> str:
        return self.administrator.username


class Teacher(models.Model):
    phone_number = models.CharField(max_length=13, verbose_name='Telefon raqam ', null=True, blank=True)
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    image = models.ImageField(upload_to='teacher/', verbose_name='Foydalanuvchi rasmi ', null=True, blank=True)
    subject = models.ManyToManyField(Lesson, related_name='teachers')

    def __str__(self) -> str:
        return self.teacher.username


class Pupil(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Ism')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Familiya')
    pupil = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pupils')
    phone_number = models.CharField(max_length=13, verbose_name='Telefon raqam ', null=True, blank=True)
    phone_number2 = models.CharField(max_length=13, verbose_name='Telefon raqam ', null=True, blank=True)
    subject = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='pupils')
    is_active = models.BooleanField(default=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='pupils')
    comment = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name}-{self.subject}'
    