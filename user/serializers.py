from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User, Administrator, Manager, Pupil, Teacher
from lesson.serializers import LessonSerializer


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'status')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super(UserSignUpSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user 

    def validate(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                {
                'status': False,
                'message': 'Bu username royhatdan o\'tgan, boshqa username kiriting!'
                }
            )
        return username   


class ManagerSerializer(serializers.ModelSerializer):
    manager = UserSignUpSerializer()
    class Meta:
        model = Manager
        fields = ('manager', 'image', 'phone_number')


class AdministratorSerializer(serializers.ModelSerializer):
    administrator = UserSignUpSerializer()
    class Meta:
        model = Administrator
        fields = ('administrator', 'image', 'phone_number')
        

class TeacherSerializer(serializers.ModelSerializer):
    subject = LessonSerializer(many=True)
    teacher = UserSignUpSerializer()
    class Meta:
        model = Teacher
        fields = ('teacher', 'image', 'phone_number', 'subject')


class PupilSerializer(serializers.ModelSerializer):
    pupil = UserSignUpSerializer()
    teacher = TeacherSerializer()
    subject = LessonSerializer()

    class Meta:
        model = Pupil
        fields = ['first_name', 'last_name', 'pupil', 'phone_number', 'phone_number2', 'subject', 'teacher']
        