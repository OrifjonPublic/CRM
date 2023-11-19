from django.shortcuts import render
from rest_framework import response, views, generics, permissions

from .models import Pupils
from .serializers import PupilRegisterSerializer

class RegisterPupilView(generics.ListCreateAPIView):
    queryset = Pupils.objects.all()
    serializer_class = PupilRegisterSerializer
    permission_classes = ( permissions.AllowAny, )


# Create your views here.
