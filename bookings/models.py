
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{'Hotel'}-{self.name}"
    
    def room_count(self):
        return self.room_set.count()
    
    def visiting_guest_count(self):
            return VisitingGuest.objects.filter(room__reservation__hotel=self).count()
    
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    capacity = models.IntegerField()
    has_room_service = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.room_number} - {self.hotel.name}"

    def visiting_guest_count(self):
        return VisitingGuest.objects.filter(room__id=self.id).count()


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
            return f"{self.guest_name} at {self.room.hotel} - Checkout at {self.check_out_date} "
    

class VisitingGuest(models.Model):
     GuestName = models.CharField(max_length=100)
     room = models.ForeignKey(Reservation, on_delete=models.CASCADE)

     def __str__(self):
          return f"Guest of {self.room.guest_name}"
     




     


