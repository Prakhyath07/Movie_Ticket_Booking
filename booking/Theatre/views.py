from django.shortcuts import render
from .models import Movies,Theatre,Halls,Seats,Show
from .serializers import (MovieSerializer, TheatreSerializer,HallsSerializer,
                        SeatsSerializer,ShowSerializer,LayoutCreateSerializer)
from rest_framework import generics

# Create your views here.

class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class TheatresList(generics.ListCreateAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer

class HallsList(generics.ListCreateAPIView):
    queryset = Halls.objects.all()
    serializer_class = HallsSerializer

class SeatsList(generics.ListCreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer

class ShowsList(generics.ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class LayoutList(generics.CreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = LayoutCreateSerializer


