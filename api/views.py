from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions

from user.models import User 
from user.serializers import UserSignUpSerializer


class UserRegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
    permission_classes = [permissions.AllowAny,]

    
# Create your views here.
