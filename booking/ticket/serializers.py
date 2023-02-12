# from .models import Users
from rest_framework import serializers
from Theatre.serializers import SeatsReadSerializer
from .models import tickets, seat_reserved
from Theatre.models import Seats,Show
from django.contrib.auth.models import User


# User Serializer


class Seat_ReservedSerializer(serializers.ModelSerializer):
    class Meta:
        model = seat_reserved
        fields = [
            "seat",]
    
class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets
        
        fields = [
            "user",
            "show",
            "count",
        ]
    
    # def create(self, validated_data):
    #     seats_data = validated_data('seats')
    #     print(seats_data)
    #     tickets = tickets.objects.create(**validated_data)
    #     return tickets

class BookTicketSerializer(serializers.Serializer):

    # count = serializers.IntegerField()
    tickets = TicketsSerializer()
    seat = Seat_ReservedSerializer()  

    def create(self , validated_data):
        ticket = validated_data.pop('tickets')
        seat = validated_data.pop('seat')
        show = ticket.get('show')
        user = ticket.get('user')
        count = ticket.get('count')
        booked_ticket=tickets.objects.create(show=show,user=user,count=count)
        seat_reserved.objects.create(seat=seat.get('seat'),show=show,tickets=booked_ticket)
      
        return {"tickets":ticket ,"seat":seat}
