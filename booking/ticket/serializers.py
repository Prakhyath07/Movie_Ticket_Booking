# from .models import Users
from rest_framework import serializers
from Theatre.serializers import SeatsReadSerializer
from .models import tickets, seat_reserved
from Theatre.models import Seats,Show
from django.contrib.auth.models import User
from user.serializers import UserPublicSerializer


# User Serializer


class Seat_ReservedSerializer(serializers.ModelSerializer):
    class Meta:
        model = seat_reserved
        fields = [
            "seat",
            "id"]
    
class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets
        
        fields = [
            "show",
        ]
class TicketsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets
        
        fields = [
        ]
    
    def create(self, validated_data):
        user = validated_data.pop("user")
        request = self.context.get("request")
        show = request.GET.get("show")
        show_instance = Show.objects.get(pk=show)
        seat = request.GET.get("seat")
        seat_instance = Seats.objects.get(pk=seat)
        ticket_instance = tickets.objects.create( show=show_instance,user=user)
        reserved_seat = seat_reserved.objects.create(seat =seat_instance,user=user,show=show_instance,tickets=ticket_instance)
        return ticket_instance
    
    
class TicketsListCreateSerializer(serializers.Serializer):
    tickets =  TicketsCreateSerializer(many = True)   

class BookTicketSerializer(serializers.Serializer):

    # count = serializers.IntegerField()
    tickets = TicketsSerializer()
    seat = Seat_ReservedSerializer() 
    user = UserPublicSerializer( read_only = True)  

    def create(self , validated_data):
        ticket = validated_data.pop('tickets')
        seat = validated_data.pop('seat')
        user = validated_data.pop('user')
        show = ticket.get('show')
        print(user)
        booked_ticket=tickets.objects.create(show=show,user=user)
        seat_reserved.objects.create(seat=seat.get('seat'),show=show,tickets=booked_ticket, user=user)
      
        return {"tickets":ticket ,"seat":seat,"user":user}
