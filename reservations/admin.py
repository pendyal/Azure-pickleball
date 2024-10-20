from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Location, Court, Reservation

admin.site.register(Location)
admin.site.register(Court)
admin.site.register(Reservation)
