from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
import json
import requests

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
    activities = trip.destination.activities.all()
    route_data = {
        "start": {"lat": trip.destination.latitude, "lng": trip.destination.longitude},
        "end": {"lat": trip.destination.latitude, "lng": trip.destination.longitude},
        "waypoints": [
            {"lat": act.latitude, "lng": act.longitude, "name": act.name}
            for act in activities
        ],
    }
    context = {"trip": trip, "route_data": json.dumps(route_data)}
    return render(request, "trip_detail.html", context)


@login_required(login_url="login")
def activity_detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, "activity_detail.html", {"activity": activity})


@require_GET
def route(request):
    start = request.GET.get("start")
    end = request.GET.get("end")
    waypoints = request.GET.get("waypoints")
    if not start or not end:
        return JsonResponse({"error": "start and end required"}, status=400)
    coords = start
    if waypoints:
        coords += ";" + waypoints
    coords += ";" + end
    url = (
        f"https://router.project-osrm.org/route/v1/driving/{coords}?overview=full&geometries=geojson"
    )
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except requests.RequestException:
        return JsonResponse({"error": "routing failed"}, status=502)
    return JsonResponse(res.json())
