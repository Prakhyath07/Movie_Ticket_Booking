from django.shortcuts import render
from .models import Movies,Theatre,Halls,Seats,Show
from .serializers import (MovieSerializer, TheatreSerializer,HallsSerializer,
                        SeatsSerializer,ShowSerializer,LayoutCreateSerializer)
from rest_framework import generics
from user.mixins import UserEditSetMixin

# Create your views here.

class MoviesList(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    
    

class TheatresList(generics.ListAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer

class HallsList(generics.ListAPIView):
    queryset = Halls.objects.all()
    serializer_class = HallsSerializer

class SeatsList(generics.ListAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer

class ShowsList(generics.ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class LayoutList(generics.ListAPIView):
    queryset = Seats.objects.all()
    serializer_class = LayoutCreateSerializer

class MoviesCreate(generics.CreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)

class TheatresCreate(generics.CreateAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)

class HallsCreate(generics.CreateAPIView):
    queryset = Halls.objects.all()
    serializer_class = HallsSerializer

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)

class SeatsCreate(generics.CreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)

class ShowsCreate(generics.CreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)

class LayoutCreate(generics.CreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = LayoutCreateSerializer

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)
    

class MoviesDetail(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class TheatresDetail(generics.RetrieveAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer

class HallsDetail(generics.RetrieveAPIView):
    queryset = Halls.objects.all()
    serializer_class = HallsSerializer

class SeatsDetail(generics.RetrieveAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer

class ShowsDetail(generics.RetrieveAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

# class LayoutDetail(generics.RetrieveAPIView):
#     queryset = Seats.objects.all()
#     serializer_class = LayoutCreateSerializer

class MoviesUpdate(UserEditSetMixin,generics.UpdateAPIView,):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class TheatresUpdate(UserEditSetMixin,generics.UpdateAPIView,):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer

class HallsUpdate(UserEditSetMixin,generics.UpdateAPIView,):
    queryset = Halls.objects.all()
    serializer_class = HallsSerializer

class SeatsUpdate(UserEditSetMixin,generics.UpdateAPIView,):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer

class ShowsUpdate(UserEditSetMixin,generics.UpdateAPIView,):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

# class LayoutUpdate(generics.UpdateAPIView,UserEditSetMixin):
#     queryset = Seats.objects.all()
#     serializer_class = LayoutCreateSerializer


class MoviesDestroy(UserEditSetMixin,generics.DestroyAPIView,):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class TheatresDestroy(UserEditSetMixin,generics.DestroyAPIView,):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer

class HallsDestroy(UserEditSetMixin,generics.DestroyAPIView,):
    queryset = Halls.objects.all()
    serializer_class = HallsSerializer

class SeatsDestroy(UserEditSetMixin,generics.DestroyAPIView,):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer

class ShowsDestroy(UserEditSetMixin,generics.DestroyAPIView,):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

# class LayoutDestroy(generics.DestroyAPIView,UserEditSetMixin):
#     queryset = Seats.objects.all()
#     serializer_class = LayoutCreateSerializer

