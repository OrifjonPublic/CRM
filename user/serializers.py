from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User, Administrator, Manager, Pupil, Teacher
from lesson.serializers import LessonSerializer


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'status')
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
    manager = UserSignUpSerializer(read_only=True)
    class Meta:
        model = Manager
        fields = ['id','phone_number',  'image', 'manager']
        extra_kwargs = {'manager': {'required': False}}

    def create(self, validated_data):
        # user = None
        request = self.context.get("request")
        user = request.user
        
        manager = Manager.objects.filter(manager=user).first()
        if manager:
            for key, value in validated_data.items():
                setattr(manager, key, value)
            manager.save()
            return manager
        manager = Manager.objects.create(manager=user, **validated_data)
        return manager


class AdministratorSerializer(serializers.ModelSerializer):
    administrator = UserSignUpSerializer(read_only=True)
    class Meta:
        model = Administrator
        fields = ( 'id','administrator', 'image', 'phone_number',)
        extra_kwargs = {'administrator': {'required': False}}
    
    def create(self, validated_data):
    
        # user = None
        request = self.context.get("request")
        user = request.user
        
        administrator = Administrator.objects.filter(administrator=user).first()
        if administrator:
            for key, value in validated_data.items():
                setattr(administrator, key, value)
            administrator.save()
            return administrator
        administrator = Administrator.objects.create(administrator=user, **validated_data)
        return administrator



class TeacherSerializer(serializers.ModelSerializer):
    subject = LessonSerializer(many=True)
    teacher = UserSignUpSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = ('teacher', 'image', 'phone_number', 'subject')
        extra_kwargs = {'administrator': {'required': False}}
    
    def create(self, validated_data):
    
        # user = None
        request = self.context.get("request")
        user = request.user
        
        teacher = Teacher.objects.filter(teacher=user).first()
        if teacher:
            for key, value in validated_data.items():
                setattr(teacher, key, value)
            teacher.save()
            return teacher
        teacher = Teacher.objects.create(teacher=user, **validated_data)
        return teacher


class PupilSerializer(serializers.ModelSerializer):
    pupil = UserSignUpSerializer()
    teacher = TeacherSerializer()
    subject = LessonSerializer()

    class Meta:
        model = Pupil
        fields = ['first_name', 'last_name', 'pupil', 'phone_number', 'phone_number2', 'subject', 'teacher']
        