from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Destination, Trip, Activity


def index(request):
    destinations = Destination.objects.all()
    return render(request, "index.html", {"destinations": destinations})


@login_required(login_url="login")
def destination(request, dest_id):
    dest = get_object_or_404(Destination, pk=dest_id)
    trips = dest.trips.all()
    activities = dest.activities.all()
    context = {"dest": dest, "trips": trips, "activities": activities}
    return render(request, "destination.html", context)


@login_required(login_url="login")
def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    return render(request, "trip_detail.html", {"trip": trip})


@login_required(login_url="login")
def activity_detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, "activity_detail.html", {"activity": activity})
