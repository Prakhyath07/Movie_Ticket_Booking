# from .models import Users
from rest_framework import serializers
from .models import tickets, seat_reserved


# User Serializer
class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets
        fields = "__name__"

class Seat_ReservedSerializer(serializers.ModelSerializer):
    class Meta:
        model = seat_reserved
        fields = "__all__"