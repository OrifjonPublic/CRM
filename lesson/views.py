from django.shortcuts import render
from rest_framework import response, permissions, views, generics

from .models import Lesson, LessonTime
from .serializers import LessonSerializer, LessonTimeSerializer


class LessonCreateListView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes= ( permissions.AllowAny, )
    

class LessonGetView(views.APIView):
    def get(self, request, id=None):
        lesson = Lesson.objects.get(id=id)
        lesson = LessonSerializer(lesson)
        return response.Response(lesson.data)


class LessonTimeView(generics.ListCreateAPIView):
    queryset = LessonTime.objects.all()
    serializer_class = LessonTimeSerializer
    permission_classes = ( permissions.AllowAny, )


class LessonTimeGetView(views.APIView):
    def get(self, request, id=None):
        timel = LessonTime.objects.get(id=id)
        timel = LessonTimeSerializer(timel)
        return response.Response(timel.data)
    

# Create your views here.
