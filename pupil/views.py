from django.shortcuts import render
from rest_framework import response, views, generics, permissions

from .models import Pupils, Room
from .serializers import PupilRegisterSerializer, RoomSerializer

class RegisterPupilView(generics.ListCreateAPIView):
    queryset = Pupils.objects.all()
    serializer_class = PupilRegisterSerializer
    permission_classes = ( permissions.AllowAny, )


class RoomView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.AllowAny,)
# Create your views here.
