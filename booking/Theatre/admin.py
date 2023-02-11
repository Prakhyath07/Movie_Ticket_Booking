from django.contrib import admin
from.models import Movies,Theatre,Halls,Seats,Show

# Register your models here.
admin.site.register([Movies,Theatre,Halls,Seats,Show])