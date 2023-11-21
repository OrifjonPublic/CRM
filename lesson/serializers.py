from rest_framework import serializers

from .models import Lesson, LessonTime


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ( 'name', 'fee' )


class LessonTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonTime
        fields = ( 'name',)
