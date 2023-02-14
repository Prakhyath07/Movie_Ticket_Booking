from django.shortcuts import render, redirect
from .models import tickets, seat_reserved
from Theatre.models import Show
from .serializers import (TicketsSerializer,TicketsCreateSerializer, Seat_ReservedSerializer,
                    BookTicketSerializer,TicketsListCreateSerializer)
from rest_framework import generics, response
from rest_framework.reverse import reverse
import urllib.parse
from user.mixins import UserQuerySetMixin
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class TicketsCreate(generics.CreateAPIView):
    queryset = tickets.objects.all()
    serializer_class = TicketsCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #     super().post(request, *args, **kwargs)
    #     user = request.POST.get('tickets.user')
    #     show = request.POST.get('tickets.show')
    #     data = {"user":user,"show":show}
    #     query_string = urllib.parse.urlencode(data)
    #     url=reverse("tickets:reserved_seats-list")+ '?{}'.format(query_string)
    #     return  redirect(url)

class ReservedSeatsList(UserQuerySetMixin,generics.ListCreateAPIView,
                        ):
    queryset = seat_reserved.objects.all()
    serializer_class = Seat_ReservedSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['id', 'show']
    


    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user)

    

    # def get_queryset(self):
    #     qs = seat_reserved.objects.all()
    #     show =self.request.GET.get('show')
    #     print(qs.filter(show= Show(pk=show)))
    #     return qs.filter(show= Show(pk=show))

class TicketsList(UserQuerySetMixin,generics.ListAPIView):
    queryset = tickets.objects.all()
    serializer_class = TicketsSerializer

class TicketsUpdate(UserQuerySetMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = tickets.objects.all()
    serializer_class = TicketsSerializer

class ReservedSeatsUpdate(UserQuerySetMixin,generics.RetrieveUpdateDestroyAPIView,
                        ):
    queryset = seat_reserved.objects.all()
    serializer_class = Seat_ReservedSerializer