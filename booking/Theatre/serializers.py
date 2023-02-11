from .models import Movies,Theatre,Halls,Seats,Show
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies

        fields = "__all__"

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre

        fields = "__all__"

class HallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Halls

        fields = "__all__"

class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats

        fields = "__all__"

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show

        fields = "__all__"

    