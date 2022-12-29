from django.urls import path, include
from .models import *
from rest_framework import routers, serializers, viewsets


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'zip', 'state', 'country', 'address']


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"
