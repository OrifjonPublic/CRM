from django.shortcuts import render
from rest_framework import response, permissions, views, generics

from .models import Lesson
from .serializers import LessonSerializer


class LessonCreateListView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes= ( permissions.AllowAny, )
    



# Create your views here.
