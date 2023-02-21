from .models import tickets, seat_reserved
from Theatre.models import Show,Seats
from Theatre.serializers import SeatsViewSerializer
from .serializers import (TicketsSerializer,TicketsCreateSerializer, Seat_ReservedSerializer
                        ,multipleticketSerializer)
from rest_framework import generics, response
from user.mixins import UserQuerySetMixin
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.expressions import Window
from django.db.models.functions import RowNumber
from django.db.models import F

# Create your views here.

class TicketsCreate(generics.CreateAPIView):
    queryset = tickets.objects.all()
    serializer_class = TicketsCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class ReservedSeatsList(UserQuerySetMixin,generics.ListCreateAPIView,
                        ):
    queryset = seat_reserved.objects.all()
    serializer_class = Seat_ReservedSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['id', 'show']
    


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

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

class multipletickets(UserQuerySetMixin,generics.CreateAPIView):
    queryset = tickets.objects.all()
    serializer_class = multipleticketSerializer

    def seats_together(self,show,count):
        show_instance = Show.objects.get(pk=show)
        hall_id = show_instance.hall.id
        reserved = seat_reserved.objects.filter(show = show).values('seat')
        

        filtered =Seats.objects.filter(hall=hall_id).exclude(id__in=reserved)
        
        numbered = filtered.annotate(row_num = Window(expression=RowNumber(),partition_by=[F('hall'),F('row'),F('column')],order_by=[F('number')]))
        
        diff=numbered.annotate(diff = F('number')-F('row_num'))  
        
        sql, params = diff.query.sql_with_params()


        together_seats = Seats.objects.raw("""
        select * from (
                SELECT *, count(*) OVER (PARTITION BY hall_id, row,column, diff
        ) AS consec_seats FROM ({}) seats_diff
            ) final where consec_seats>=%s """.format(sql)%(*params,count),
        )
        return together_seats

    def multi_ticket(self, serializer):

        show=self.request.GET.get('show')
        count =int(self.request.POST.get('count'))

        seats_friends = self.seats_together(show,count)
        
        if len(seats_friends) ==0:
            for i in Show.objects.all():
                
                other_seats_friends = self.seats_together(i.id,count)

                if len(other_seats_friends)>0:
                    print(i.movie, i.start_time)
                    output = f"As {count} no. of tickets are not available for this show you can checkout the movie {i.movie} at time {i.start_time}"
                    return output
            else:
                output = f"{count} number of tickets are not available for any show"
                return output
        
        else:
            output= list(seats_friends)[:count]
            serializer = SeatsViewSerializer(output,many=True)
            print(serializer.data)
            
            return serializer.data
        
    def create(self, request, *args, **kwargs):
        output = self.multi_ticket(request)
        if isinstance(output,str):
            return response.Response({"output":output})
        
        else:
            seat =[]
            show=self.request.GET.get('show')
            show_instance =Show.objects.get(pk=show)
            user = self.request.user
            booked_ticket=tickets.objects.create(show=show_instance,user=user)
            for i in output:
                seat.append(i.get('pk'))
                seat_instance = Seats.objects.get(pk =i.get('pk') )
                seat_reserved.objects.create(seat=seat_instance,show=show_instance,tickets=booked_ticket, user=user)
    
            count =int(self.request.POST.get('count'))
            tickets_list = [f"row:{i.get('row')}, number:{i.get('number')}" for i in output]
            print(tickets_list)
            tickets_str = ','.join(tickets_list)
            return response.Response({"output":f"{count} tickets successfully booked:{tickets_str}"})



    

    


    