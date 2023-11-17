# bookings/views.py
from django.shortcuts import render, redirect
from .forms import HotelForm, RoomForm, ReservationForm
from .models import *

def hotel_list(request):
    hotels = Hotel.objects.all()
    hotel_room_counts = {hotel.id: hotel.room_set.count() for hotel in hotels}
    print(hotel_room_counts)
    return render(request, 'hotel_list.html', {'hotels': hotels, 'room_counts': hotel_room_counts})

def add_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')
    else:
        form = HotelForm()    
        all_hotels = Hotel.objects.all()

        for hotel in all_hotels:
           print(f"Hotel: {hotel.name}")
           print(f"Number of rooms: {hotel.room_count()}")
           print(f"Number of visiting guests: {hotel.visiting_guest_count()}")
           print("\n")
    return render(request, 'add_hotel.html', {'form': form})


