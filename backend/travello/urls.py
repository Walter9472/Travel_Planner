from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destination/<int:dest_id>/', views.destination, name='destination'),
    path('trip/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('activity/<int:activity_id>/', views.activity_detail, name='activity_detail'),

]
