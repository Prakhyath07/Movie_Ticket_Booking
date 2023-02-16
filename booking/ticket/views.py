from django.shortcuts import render, redirect
from .models import tickets, seat_reserved
from Theatre.models import Show,Seats
from Theatre.serializers import SeatsViewSerializer
from .serializers import (TicketsSerializer,TicketsCreateSerializer, Seat_ReservedSerializer
                        ,multipleticketSerializer,multipleticketBookSerializer)
from rest_framework import generics, response
from rest_framework.reverse import reverse
from user.mixins import UserQuerySetMixin
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.expressions import Window
from django.db.models.functions import RowNumber
from django.db.models import F,Count
from django.forms.models import model_to_dict
from django.http import QueryDict

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

class multipleticets(UserQuerySetMixin,generics.CreateAPIView):
    queryset = tickets.objects.all()
    serializer_class = multipleticketSerializer

    def multi_ticket(self, serializer):
        # serializer.save(user = self.request.user)
        show=self.request.GET.get('show')
        count =int(self.request.POST.get('count'))
        show_instance = Show.objects.get(pk=show)
        hall_id = show_instance.hall.id
        reserved = seat_reserved.objects.filter(show = show).values('seat')
        

        filtered =Seats.objects.filter(hall=hall_id).exclude(id__in=reserved)
        
        numbered = filtered.annotate(row_num = Window(expression=RowNumber(),partition_by=[F('hall'),F('row'),F('column')],order_by=[F('number')]))
        
        diff=numbered.annotate(diff = F('number')-F('row_num'))  
        
        sql, params = diff.query.sql_with_params()


        seats_friends = Seats.objects.raw("""
        select * from (
                SELECT *, count(*) OVER (PARTITION BY hall_id, row,column, diff
        ) AS consec_seats FROM ({}) seats_diff
            ) final where consec_seats>=%s """.format(sql)%(*params,count),
        )
        
        if len(seats_friends) ==0:
            for i in Show.objects.all():
                show=i.id
                show_instance = Show.objects.get(pk=show)
                hall_id = show_instance.hall.id
                reserved = seat_reserved.objects.filter(show = show).values('seat')
                

                filtered =Seats.objects.filter(hall=hall_id).exclude(id__in=reserved)
                
                numbered = filtered.annotate(row_num = Window(expression=RowNumber(),partition_by=[F('hall'),F('row'),F('column')],order_by=[F('number')]))
                
                diff=numbered.annotate(diff = F('number')-F('row_num'))  
                
                sql, params = diff.query.sql_with_params()


                other_seats_friends = Seats.objects.raw("""
                select * from (
                        SELECT *, count(*) OVER (PARTITION BY hall_id, row,column, diff
                ) AS consec_seats FROM ({}) seats_diff
                    ) final where consec_seats>=%s """.format(sql)%(*params,count),
                )

                if len(other_seats_friends)>0:
                    print(i.movie, i.start_time)
                    output = f"As {count} no. of tickets are not available for this show you can checkout the movie {i.movie} at time {i.start_time}"
                    return output
            else:
                output = f"{count} number of tickets are not available for any show"
                return output
        
        else:
            output= list(seats_friends)[:count]
            # output = Seats.objects.filter(hall=3)
            # print(output[0].id)
            # # qs_dict = model_to_dict(seats_friends)
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
            print("user",user)
            booked_ticket=tickets.objects.create(show=show_instance,user=user)
            for i in output:
                seat.append(i.get('pk'))
                seat_instance = Seats.objects.get(pk =i.get('pk') )
                seat_reserved.objects.create(seat=seat_instance,show=show_instance,tickets=booked_ticket, user=user)
            query_dictionary = QueryDict('', mutable=True)
            query_dictionary.update(
            {
            'seat': seat,
            "show":show
            }
            )
            url = '{base_url}?{querystring}'.format(
            base_url=reverse("tickets:tickets-multiplecreate", request= request),
            querystring=query_dictionary.urlencode()
            )
            count =int(self.request.POST.get('count'))
            return response.Response({"output":f"{count} tickets successfully booked:{output}"})


class multipleseatbook(generics.CreateAPIView):

    queryset = Seats.objects.all()
    serializer_class = multipleticketBookSerializer

    

    


    