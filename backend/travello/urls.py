from django.urls import path
from . import views

# Map URL patterns to their respective view functions.
urlpatterns = [
    # Landing page with all destinations
    path('', views.index, name='index'),
    # Detail pages for destinations, trips and activities
    path('destination/<int:dest_id>/', views.destination, name='destination'),
    path('trip/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('activity/<int:activity_id>/', views.activity_detail, name='activity_detail'),
    # Simple REST endpoint returning route information as JSON
    path('api/route/', views.route, name='api_route'),

]
