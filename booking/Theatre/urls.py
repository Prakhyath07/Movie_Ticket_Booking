from django.urls import path, include
from . import views


app_name = "Theatre"
urlpatterns = [
    path("shows/", views.ShowsList.as_view(), name="shows-list"),
    path("movies/", views.MoviesList.as_view(), name="movies-list"),
    path("theatres/", views.TheatresList.as_view(), name="theatres-list"),
    path("seats/", views.SeatsList.as_view(), name="seats-list"),
    path("halls/", views.HallsList.as_view(), name="halls-list"),
    path("layout/", views.LayoutList.as_view(), name="layout-list"),

    path("shows/create", views.ShowsCreate.as_view(), name="shows-create"),
    path("movies/create", views.MoviesCreate.as_view(), name="movies-create"),
    path("theatres/create", views.TheatresCreate.as_view(), name="theatres-create"),
    path("seats/create", views.SeatsCreate.as_view(), name="seats-create"),
    path("halls/create", views.HallsCreate.as_view(), name="halls-create"),
    path("layout/create", views.LayoutCreate.as_view(), name="layout-create"),

    path("shows/<int:pk>", views.ShowsDetail.as_view(), name="shows-detail"),
    path("movies/<int:pk>", views.MoviesDetail.as_view(), name="movies-detail"),
    path("theatres/<int:pk>", views.TheatresDetail.as_view(), name="theatres-detail"),
    path("seats/<int:pk>", views.SeatsDetail.as_view(), name="seats-detail"),
    path("halls/<int:pk>", views.HallsDetail.as_view(), name="halls-detail"),
    # path("layout/<int:pk>", views.LayoutDetail.as_view(), name="layout-detail"),

    path("shows/<int:pk>/update", views.ShowsUpdate.as_view(), name="shows-update"),
    path("movies/<int:pk>/update", views.MoviesUpdate.as_view(), name="movies-update"),
    path("theatres/<int:pk>/update", views.TheatresUpdate.as_view(), name="theatres-update"),
    path("seats/<int:pk>/update", views.SeatsUpdate.as_view(), name="seats-update"),
    path("halls/<int:pk>/update", views.HallsUpdate.as_view(), name="halls-update"),
    # path("layout/<int:pk>/update", views.LayoutUpdate.as_view(), name="layout-update"),

    path("shows/<int:pk>/delete", views.ShowsDestroy.as_view(), name="shows-delete"),
    path("movies/<int:pk>/delete", views.MoviesDestroy.as_view(), name="movies-delete"),
    path("theatres/<int:pk>/delete", views.TheatresDestroy.as_view(), name="theatres-delete"),
    path("seats/<int:pk>/delete", views.SeatsDestroy.as_view(), name="seats-delete"),
    path("halls/<int:pk>/delete", views.HallsDestroy.as_view(), name="halls-delete"),
    # path("layout/<int:pk>/delete", views.LayoutDestroy.as_view(), name="layout-delete"),
    
]