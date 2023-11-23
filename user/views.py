from django.shortcuts import render
from rest_framework import response, generics, permissions, views
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from .models import User, Teacher, Pupil, Manager, Administrator
from .serializers import UserSignUpSerializer, ManagerSerializer, TeacherSerializer, PupilSerializer, AdministratorSerializer

class UserRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
    lookup_field = 'id' 
    permission_classes = [permissions.AllowAny]


class UserManagerView(views.APIView):
    parser_classes = [MultiPartParser, JSONParser, FormParser]

    def get(self, request):
        user = Manager.objects.filter(manager=request.user).first()
        serializer = ManagerSerializer(user)
        return response.Response(serializer.data)
    
    def post(self, request):
        serializer = ManagerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response({
            "message": "xato bor .",
             "errors": [i for i in serializer.errors]
        })


class UserAdministratorView(views.APIView):
    parser_classes = [MultiPartParser, JSONParser, FormParser]

    def get(self, request):
        user = Administrator.objects.filter(administrator=request.user).first()
        serializer = ManagerSerializer(user)
        return response.Response(serializer.data)
    
    def post(self, request):
        serializer = AdministratorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response({
            "message": "xato bor .",
             "errors": [i for i in serializer.errors]
        })

# Create your views here.

class RequestUserStatView(views.APIView):
    def get(self, request):
        user = request.user
        serializer = UserSignUpSerializer(user)
        return response.Response(serializer.data)
