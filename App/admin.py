from django.contrib import admin

# Register your models here.
from App.models import Car_w, Car, Parking

admin.site.register(Car_w)
admin.site.register(Car)
admin.site.register(Parking)