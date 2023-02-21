# from .models import Users
from rest_framework import serializers
from .models import tickets, seat_reserved
from Theatre.models import Seats,Show


# User Serializer
class Seat_ReservedSerializer(serializers.ModelSerializer):
    class Meta:
        model = seat_reserved
        fields = [
            "seat",
            "id"]
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['seat'] = instance.seat.__str__()
        return rep
    
class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets
        
        fields = "__all__"
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['show'] = instance.show.__str__()
        return rep

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

class multipleticketSerializer(serializers.Serializer):

    count = serializers.IntegerField()

