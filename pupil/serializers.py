from rest_framework import serializers

from .models import Pupils


class PupilRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupils
        fields = (
            'first_name',
            'last_name',
            'subject',
            'phone_number_1',
            'phone_number_2',
            'lesson_day',
            'lesson_time',
            'comment',
              )
    