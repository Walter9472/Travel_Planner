from django.urls import path
from . import views

# URLs for user authentication views
urlpatterns = [
    path('register', views.register, name='register'),  # registration form
    path('login', views.login, name='login'),  # login form
    path('logout', views.logout, name='logout'),  # logout and redirect
]
