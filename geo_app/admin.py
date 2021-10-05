from django.contrib import admin
from geo_app.models import Place
from leaflet.admin import LeafletGeoAdmin


@admin.register(Place)
class PlaceAdmin(LeafletGeoAdmin):
    list_display = ['name', 'location']
