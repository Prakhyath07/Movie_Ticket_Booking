from django.urls import path, include
from . import views


app_name = "Theatre"
urlpatterns = [
    path("", views.ShowsList.as_view(), name="shows-list"),
    path("movies/", views.MoviesList.as_view(), name="movies-list"),
    path("theatres/", views.TheatresList.as_view(), name="theatres-list"),
    path("seats/", views.SeatsList.as_view(), name="seats-list"),
    path("halls/", views.HallsList.as_view(), name="halls-list"),
    path("layout/", views.LayoutList.as_view(), name="layout-list"),
]