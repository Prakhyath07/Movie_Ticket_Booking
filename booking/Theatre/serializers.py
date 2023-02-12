from .models import Movies,Theatre,Halls,Seats,Show
from rest_framework import serializers
from user.serializers import UserPublicSerializer

from .validators import validate_min_value


class MovieSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer( read_only = True)
    class Meta:
        model = Movies

        fields = [
            "title",
            "language",
            "duration",
            "user"
        ]
        
class HallsSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer( read_only = True)
    location = serializers.CharField(source = 'theatre.location', required =False,read_only = True)
    class Meta:
        model = Halls

        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['theatre'] = instance.theatre.name
        return rep
        
class TheatreSerializer(serializers.ModelSerializer):
    # user = UserPublicSerializer( read_only = True)
    class Meta:
        model = Theatre

        fields = [
            "name",
            "location",
        ]

class SeatsSerializer(serializers.ModelSerializer):
    # user = UserPublicSerializer( read_only = True)
    theatre = serializers.CharField(source = 'hall.theatre', required =False,read_only = True)
    
    class Meta:

        model = Seats

        fields = [
            "row",
            "number",
            "hall",
            "theatre"

        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['hall'] = instance.hall.name
        return rep

class ShowSerializer(serializers.ModelSerializer):
    # user = UserPublicSerializer( read_only = True)
    theatre = serializers.CharField(source = 'hall.theatre', required =False,read_only = True)
    language = serializers.CharField(source = 'movie.language', required =False,read_only = True)
    class Meta:
        model = Show

        fields = [
            "movie",
            "language",
            "start_time",
            "cost",
            "theatre",
            "hall",
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['hall'] = instance.hall.name
        rep['movie'] = instance.movie.title
        return rep

class SeatsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats

        fields = ["hall"]


class LayoutCreateSerializer(serializers.Serializer):
    
    num_seats_per_row = serializers.IntegerField(validators = [validate_min_value])
    num_rows = serializers.IntegerField()
    # theatre = TheatreSerializer()
    seat = SeatsReadSerializer() 
    user = UserPublicSerializer( read_only = True) 

    def create(self , validated_data):
        num_rows = validated_data.pop('num_rows')
        num_seats_per_row = validated_data.pop('num_seats_per_row')
        hall = validated_data.pop('seat')
        hall_instance = hall.get('hall')
        seats_per_col = num_seats_per_row//3
        seats_objs = []
        user = validated_data.pop('user')
        for i in range(1,num_rows+1):
            for j in range(1,seats_per_col+1):
                seats_obj_A = Seats.objects.create(number =j,row=i, column='A',hall = hall_instance, user = user)
                seats_objs.append(seats_obj_A)
                seats_obj_B = Seats.objects.create(number =j+seats_per_col,row=i, column='B',hall = hall_instance, user = user)
                seats_objs.append(seats_obj_B)
                seats_obj_C = Seats.objects.create(number =j+(2*seats_per_col),row=i, column='C',hall = hall_instance, user = user)
                seats_objs.append(seats_obj_C)

        
        return {"num_seats_per_row":num_seats_per_row ,"num_rows":num_rows,"seat":hall}

    
