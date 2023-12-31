from rest_framework_simplejwt.views import (    TokenObtainPairView, TokenRefreshView, )

from django.urls import path

from .views import UserRegisterView

from user.views import UserRetrieveView, UserManagerView, RequestUserStatView, UserAdministratorView

from lesson.views import LessonCreateListView, LessonTimeView, LessonGetView, LessonTimeGetView

from pupil.views import RegisterPupilView, RoomView

urlpatterns = [


    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),

    #request user
    path('request/user/', RequestUserStatView.as_view(), name='request_user'),
    path('user/<int:id>/', UserRetrieveView.as_view(), name='user_retrieve'),
    path('manager/', UserManagerView.as_view(), name='manager'),
    path('administrator/', UserAdministratorView.as_view(), name='administrator'),


    # Lesson
    path('lesson/', LessonCreateListView.as_view(), name='lesson_create'),
    path('lesson/<int:id>/', LessonGetView.as_view(), name='lesson_detail'),
    path('lesson/time/<int:id>/', LessonTimeGetView.as_view(), name='lesson_time_detail'),

    #PupilsRegister
    path('register_pupil/', RegisterPupilView.as_view(), name='register_pupils'),

    #room
    path('room/', RoomView.as_view(), name='room_create'),

    #lessonTime
    path('lesson/time/', LessonTimeView.as_view(), name='lesson_time'),
]