from rest_framework_simplejwt.views import (
                                                TokenObtainPairView,
                                                TokenRefreshView,
                                            )

from django.urls import path
from .views import UserRegisterView


urlpatterns = [


    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]