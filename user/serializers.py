from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


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
