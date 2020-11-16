from django.contrib import admin

from .models import NatParks, NatParkGeo

# Register your models here.


class NatParkGeoAdmin(admin.ModelAdmin):
    list_display = ['calltitle', 'state']


admin.site.register(NatParks)
admin.site.register(NatParkGeo,  NatParkGeoAdmin)

