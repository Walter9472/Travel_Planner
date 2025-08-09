from django.contrib import admin

from .models import Destination, Trip, Activity


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ("title", "destination", "start_date", "end_date")


admin.site.register(Destination)
admin.site.register(Activity)

