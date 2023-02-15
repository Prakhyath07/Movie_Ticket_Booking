from django.urls import path, include
from . import views


app_name = "tickets"
urlpatterns = [
    path("", views.TicketsCreate.as_view(), name="tickets-create"),
    path("reserved_seats/", views.ReservedSeatsList.as_view(), name="reserved_seats-list"),
    path("ticketslist/", views.TicketsList.as_view(), name="tickets-list"),
    path("reserved_seats/<int:pk>", views.ReservedSeatsUpdate.as_view(), name="reserved_seats-update"),
    path("ticketsupdate/<int:pk>", views.TicketsUpdate.as_view(), name="tickets-update"),
    path("multiple/", views.multipleticets.as_view(), name="tickets-multiple"),
    path("multipleview/", views.multipleViewtickets.as_view(), name="tickets-multipleview"),
]