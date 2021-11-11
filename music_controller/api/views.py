from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Room
from .serializers import RoomSerializer

class RoomView(generics.CreateAPIView):
    QuerySet = Room.objects.all()
    serializer_class = RoomSerializer

