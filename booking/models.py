from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    type = models.CharField(max_length=120)
    location = models.TextField()
    features = models.TextField()
    price = models.DecimalField(decimal_places=2)

    def __str__(self):
        return f"Room №{self.number} – {self.capacity}"

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)