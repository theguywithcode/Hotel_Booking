# bookings/urls.py
from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "Hotel Booking Admin"
admin.site.site_title = "Hotel Booking Portal"
admin.site.index_title = "Welcome to Hotel Booking Portal"

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('add_hotel/', views.add_hotel, name='add_hotel'),
    # Add more paths for other views
]
