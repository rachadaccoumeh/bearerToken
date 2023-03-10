"""barearToken URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers

from app.views import LocationViewSet, HospitalViewSet, location_add, hospital_add, location_delete

router = routers.DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'hospital', HospitalViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apiauthentication.urls')),
    path('', include(router.urls)),
    path('add-location', location_add),
    path('add-hospital', hospital_add),
    path('delete-location/<int:pk>', location_delete),

]
