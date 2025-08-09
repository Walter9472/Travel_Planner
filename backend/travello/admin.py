from django.contrib import admin

from .models import Destination, Trip, Activity

# Register your models here.
admin.site.register(Trip)
admin.site.register(Destination)
admin.site.register(Activity)

