from django.shortcuts import render
from rest_framework import response, permissions, views, generics

from .models import Lesson, LessonTime
from .serializers import LessonSerializer, LessonTimeSerializer


class LessonCreateListView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes= ( permissions.AllowAny, )
    

class LessonTimeView(generics.ListCreateAPIView):
    queryset = LessonTime.objects.all()
    serializer_class = LessonTimeSerializer
    permission_classes = ( permissions.AllowAny, )


# Create your views here.
