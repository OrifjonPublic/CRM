from rest_framework import serializers

from .models import Pupils, Room
from lesson.serializers import LessonSerializer


class PupilRegisterSerializer(serializers.ModelSerializer):
    # subject = LessonSerializer()
    
    class Meta:
        model = Pupils
        fields = (
            'id',
            'first_name',
            'last_name',
            'subject',
            'phone_number_1',
            'phone_number_2',
            'lesson_day',
            'lesson_time',
            'comment',
              )

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('name', 'id')    