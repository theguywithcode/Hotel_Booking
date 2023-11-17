# bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('add_hotel/', views.add_hotel, name='add_hotel'),
    # Add more paths for other views
]
