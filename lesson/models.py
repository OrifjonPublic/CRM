from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    fee = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name.title()
    