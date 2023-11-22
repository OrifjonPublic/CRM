from django.shortcuts import render
from rest_framework import response, generics, permissions, views
from rest_framework.parsers import MultiPartParser

from .models import User, Teacher, Pupil, Manager, Administrator
from .serializers import UserSignUpSerializer, ManagerSerializer, TeacherSerializer, PupilSerializer, AdministratorSerializer

class UserRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
    lookup_field = 'id' 
    permission_classes = [permissions.AllowAny]


class UserManagerView(views.APIView):
    parser_classes = [MultiPartParser]

    def get(self, request):
        user = Manager.objects.get(manager=request.user)
        serializer = ManagerSerializer(user)
        return response.Response(serializer.data)
    
    # def post(self, request):
    #     serializer = ManagerSerializer(data=request.data)
    #     return response.Response()
# Create your views here.

class RequestUserStatView(views.APIView):
    def get(self, request):
        user = request.user
        serializer = UserSignUpSerializer(user)
        return response.Response(serializer.data)
