from .models import Movies,Theatre,Halls,Seats,Show
from rest_framework import serializers
from user.serializers import UserPublicSerializer
from rest_framework.reverse import reverse
from ticket.models import seat_reserved
from django.http import QueryDict

from .validators import validate_min_value


class MovieSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='Theatre:movies-detail',
        lookup_field = 'pk'
    )
    # user = UserPublicSerializer( read_only = True)
    class Meta:
        model = Movies

        fields = [
            "title",
            "language",
            "duration",
            "url"
        ]
        
        

class MovieDetailSerializer(serializers.ModelSerializer):

    # shows = serializers.ListField(child =serializers.CharField(max_length=100))
    shows = serializers.SerializerMethodField(read_only=True)
    

    class Meta:
        model = Movies

        fields = [
            "title",
            "language",
            "duration",
            "shows"
        ]
    
    def get_shows(self,obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Movies):
            return None
        # print(self.context)
        request = self.context.get('request')
        shows = Show.objects.filter(movie=obj)
        context={'request': request},
        res = ShowSerializer(shows,many=True,context=context)
        # print(res.data)
        return res.data
        
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
    url = serializers.SerializerMethodField(read_only= True)
    theatre = serializers.CharField(source = 'hall.theatre', required =False,read_only = True)
    
    class Meta:

        model = Seats

        fields = [
            "pk",
            "row",
            "number",
            "hall",
            "theatre",
            "column",
            "url"

        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['hall'] = instance.hall.name
        return rep
    
    def get_url(self,obj):
        request = self.context.get('request')
        seat = obj.id
        show = self.context.get('show')
        print(seat)
        print(show)
        if request is None:
            return None
        query_dictionary = QueryDict('', mutable=True)
        query_dictionary.update(
        {
        'seat': seat,
        "show":show
        }
        )
        url = '{base_url}?{querystring}'.format(
            base_url=reverse("tickets:tickets-create", request= request),
            querystring=query_dictionary.urlencode()
            )
        
        # return reverse("tickets:tickets-create", request= request)
        return url

class ShowSerializer(serializers.ModelSerializer):

    # url = serializers.HyperlinkedIdentityField(
    #     view_name='Theatre:shows-detail',
    #     lookup_field = 'pk'
    # )
    url = serializers.SerializerMethodField(read_only= True)
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
            "url",
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['hall'] = instance.hall.name
        rep['movie'] = instance.movie.title
        return rep
    
    def get_url(self,obj):
        # print(obj)
        print(self)
        request = self.context[0].get('request')
        # print(request)
        if request is None:
            return None
        return reverse("Theatre:shows-detail", kwargs={"pk":obj.pk}, request= request)

class ShowDetailSerializer(serializers.ModelSerializer):
    seats = serializers.SerializerMethodField(read_only=True)
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
            "seats",
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['hall'] = instance.hall.name
        rep['movie'] = instance.movie.title
        return rep
    
    def get_seats(self,obj):
        request = self.context.get('request')
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Show):
            return None
        Hall_instance = Halls.objects.get(pk=obj.hall.id)
        reserved = seat_reserved.objects.filter(show = obj.id).values('seat')
        # print(reserved)
        seats = Seats.objects.filter(hall=Hall_instance).exclude(id__in=reserved)
        # print(list(seats.values('pk')))
        context={'request': request, "show":obj.id}
        res = SeatsSerializer(seats,many=True,context=context)
        return res.data

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

    
