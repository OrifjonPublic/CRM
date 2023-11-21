from collections.abc import Iterable
from django.db import models
from lesson.models import Lesson, LessonTime
from user.models import Teacher, Pupil, User

import random

class Pupils(models.Model):
    
    DAY = (
        ('Dushanba', 'DU-CHOR-JUMA'),
        ('Seshanba', 'SE-PAY-SHANBA'),
    )

    first_name = models.CharField(max_length=50, verbose_name='Ism', null=True,blank=True)
    last_name = models.CharField(max_length=50, verbose_name='Familiya', null=True,blank=True)
    subject = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='register_pupils', verbose_name='Yo\'nalish')
    phone_number_1 = models.CharField(max_length=13, verbose_name='1-telefon raqam')
    phone_number_2 = models.CharField(max_length=13, verbose_name='2-telefon raqam', null=True, blank=True)
    lesson_day = models.CharField(max_length=30, choices=DAY, default='Dushanba', blank=True, null=True, verbose_name="Kun")
    lesson_time = models.CharField(max_length=300, null=True, blank=True, verbose_name='Sizga qulay dars vaqti')
    comment = models.CharField(max_length=200, verbose_name='Kim tavsiya berdi', null=True, blank=True)
    is_active_pupil = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name} - {self.subject}'
    

class Room(models.Model):
    name = models.CharField(max_length=30, verbose_name='xona')

    def __str__(self) -> str:
        return self.name


class Group(models.Model):
    DAY = (
        ('dushanba',  'DUSHANBA'),
        ('seshanba',  'SESHANBA'),
    )
    

    name = models.CharField(max_length=120, unique=True, blank=True, verbose_name='guruh nomi')
    day = models.CharField(max_length=30, choices=DAY)
    pupils = models.ManyToManyField(Pupil)
    subject = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Yo\'nalish')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='groups', verbose_name='dars xonasi')
    vaqt = models.ForeignKey(LessonTime, on_delete=models.CASCADE, verbose_name='dars vaqti', null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Ustoz')

    def save(self, *args, **kwargs):
        if not self.name:
            fan = self.subject.name.split()
            name = ''
            for i in fan:
                if len(fan)==1:
                    name += i[0:2].title()
                else:   
                    name += i[0].title()
            self.name = name + '-' + str(random.randint(10000,99999))
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.name}'


# class GroupPupil(models.Model):

#     DAY = (
#         ('dushanba',  'DUSHANBA'),
#         ('seshanba',  'SESHANBA'),
#     )

#     pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE, related_name='pupils')
#     group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='group')
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='groups')
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='groups')
#     subject = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='groups')
#     created = models.DateTimeField(auto_now_add=True)
#     day = models.CharField(max_length=30, choices=DAY)

#     def __str__(self) -> str:
#         return f'{self.group}-{self.subject}'
    