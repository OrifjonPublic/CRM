from rest_framework_simplejwt.views import (    TokenObtainPairView, TokenRefreshView, )

from django.urls import path

from .views import UserRegisterView
from lesson.views import LessonCreateListView
from pupil.views import RegisterPupilView

urlpatterns = [


    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),

    # Lesson
    path('lesson/', LessonCreateListView.as_view(), name='lesson_create'),

    #PupilsRegister
    path('register_pupil/', RegisterPupilView.as_view(), name='register_pupils'),

]