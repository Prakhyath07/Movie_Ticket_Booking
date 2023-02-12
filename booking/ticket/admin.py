from django.contrib import admin
from .models import seat_reserved,tickets

# Register your models here.
admin.site.register([seat_reserved,tickets])