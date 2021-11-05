from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics

from .models import Room
from .serializers import RoomSerializer

class RoomView(generics.CreateAPIView):
    QuerySet = Room.objects.all()
    serializer_class = RoomSerializer