# bookings/forms.py
from django import forms
from .models import Hotel, Room, Reservation

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'address']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['hotel', 'room_number', 'capacity','has_room_service']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'guest_name', 'check_in_date', 'check_out_date']
