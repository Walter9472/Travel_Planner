from django.contrib import admin

from .models import Destination, Trip, Activity

# Register your models here.

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ("title", "destination", "start_date", "end_date")

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("name", "desc")
    search_fields = ("name", "desc")


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "desc","price")
    search_fields = ("name", "country")

