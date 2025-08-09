from django.http import HttpResponse


def index(request):
    """Return a simple greeting for the Travello app."""
    return HttpResponse("Welcome to Travello!")

