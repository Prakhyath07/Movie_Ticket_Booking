from django.shortcuts import render
from .models import tickets, seat_reserved
from .serializers import TicketsSerializer, Seat_ReservedSerializer,BookTicketSerializer
from rest_framework import generics

# Create your views here.

class TicketsList(generics.CreateAPIView):
    queryset = tickets.objects.all()
    serializer_class = BookTicketSerializer

class ReservedSeatsList(generics.ListCreateAPIView):
    queryset = seat_reserved.objects.all()
    serializer_class = Seat_ReservedSerializer
