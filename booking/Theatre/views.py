from django.shortcuts import render
from .models import Movies,Theatre,Halls,Seats,Show
from .serializers import (MovieSerializer, TheatreSerializer,HallsSerializer,
                        SeatsSerializer,ShowSerializer,LayoutCreateSerializer,MovieDetailSerializer,
                        ShowDetailSerializer,SeatsViewSerializer,TheatreViewSerializer,HallsViewSerializer,
                        HallsListSerializer,ShowsListSerializer,ShowsCreateSerializer,SeatsUpdateSerializer)
from rest_framework import generics
from user.mixins import UserEditSetMixin
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework import status

# Create your views here.

class MoviesList(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    
    

class TheatresList(generics.ListAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer

class HallsList(generics.ListAPIView):
    queryset = Halls.objects.all()
    serializer_class = HallsListSerializer

class SeatsList(generics.ListAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsViewSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['id', 'hall']

class ShowsList(generics.ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowsListSerializer

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
    serializer_class = HallsListSerializer

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)

class SeatsCreate(generics.CreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsViewSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['id', 'hall']

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)

class ShowsCreate(generics.CreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowsCreateSerializer

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)

class LayoutCreate(generics.CreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = LayoutCreateSerializer

    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)
    

class MoviesDetail(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieDetailSerializer

    # def get(self, request, *args, **kwargs):
    #     serializer_context = {
    #         'request': None,
    #     }
    #     movie = get_object_or_404(Movies, pk=2)
    #     print(movie)
    #     serializer_class = MovieDetailSerializer(self.get_queryset(),many=True,context=serializer_context)
    #     print(serializer_class.data)
    #     return Response(serializer_class.data)


class TheatresDetail(generics.RetrieveAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreViewSerializer

class HallsDetail(generics.RetrieveAPIView):
    queryset = Halls.objects.all()
    serializer_class = HallsViewSerializer

class SeatsDetail(generics.RetrieveAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsViewSerializer

class ShowsDetail(generics.RetrieveAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowDetailSerializer

    # def get(self, request, *args, **kwargs):
    #     serializer_context = {
    #         'request': None,
    #     }
    #     movie = get_object_or_404(Movies, pk=2)
    #     print(movie)
    #     serializer_class = ShowSerializer(self.get_queryset(),many=True,context=serializer_context)
    #     print(serializer_class.data)
    #     return Response(serializer_class.data)

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
    serializer_class = HallsListSerializer

class SeatsUpdate(UserEditSetMixin,generics.UpdateAPIView,):
    queryset = Seats.objects.all()
    serializer_class = SeatsUpdateSerializer


    # def update(self, request, *args, **kwargs):
    #     obj =self.get_object()
    #     hall_id = Seats.objects.get(pk=obj.id).hall.id
    #     row_id = Seats.objects.get(pk=obj.id).row
    #     column_val = Seats.objects.get(pk=obj.id).column
    #     counts =Seats.objects.filter(hall=hall_id,row=row_id).values('column').annotate(total=Count('id'))
    #     map_dict = {'A':0,'B':1,'C':2}
    #     value =counts[map_dict[column_val]].get('total')
    #     statement ={"hall_id":hall_id,"column_val":column_val,"counts":counts,"value":value}
    #     print(statement)
    #     if value==2:
    #         return Response(data={'message': "minimun 2 seats per column required "},
    #                         status=status.HTTP_400_BAD_REQUEST)
        
    #     self.perform_update(obj)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class ShowsUpdate(UserEditSetMixin,generics.UpdateAPIView,):
    queryset = Show.objects.all()
    serializer_class = ShowsListSerializer

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
    serializer_class = SeatsViewSerializer

    def destroy(self, request, *args, **kwargs):
        obj =self.get_object()
        hall_id = Seats.objects.get(pk=obj.id).hall.id
        row_id = Seats.objects.get(pk=obj.id).row
        column_val = Seats.objects.get(pk=obj.id).column
        counts =Seats.objects.filter(hall=hall_id,row=row_id).values('column').annotate(total=Count('id'))
        map_dict = {'A':0,'B':1,'C':2}
        value =counts[map_dict[column_val]].get('total')
        statement ={"hall_id":hall_id,"column_val":column_val,"counts":counts,"value":value}
        print(statement)
        if value==2:
            return Response(data={'message': "minimun 2 seats per column required "},
                            status=status.HTTP_400_BAD_REQUEST)

        self.perform_destroy(obj)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShowsDestroy(UserEditSetMixin,generics.DestroyAPIView,):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

# class LayoutDestroy(generics.DestroyAPIView,UserEditSetMixin):
#     queryset = Seats.objects.all()
#     serializer_class = LayoutCreateSerializer

