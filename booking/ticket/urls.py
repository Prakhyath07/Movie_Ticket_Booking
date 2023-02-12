from django.urls import path, include
from . import views


app_name = "tickets"
urlpatterns = [
    path("", views.TicketsList.as_view(), name="tickets-list"),
    path("reserved_seats/", views.ReservedSeatsList.as_view(), name="reserved_seats-list"),
]