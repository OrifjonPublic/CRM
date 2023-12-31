"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework import permissions
from django.conf.urls.static import static
from rest_framework import permissions


sxema = get_schema_view(
    openapi.Info(
        title="CRM",
        description="Itschool",
        default_version="1.0.0",
        terms_of_service="https://www.google.com/policies/terms",
        contact=openapi.Contact(email='orifjonqahhorov57@gmail.com'),
        license=openapi.License(name="Project litsenziyasi")),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path("swagger/", sxema.with_ui('swagger', cache_timeout=0), name="swagger"),
    path("redoc/", sxema.with_ui('redoc', cache_timeout=0), name="redoc"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
