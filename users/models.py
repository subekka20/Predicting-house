from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=15)
    USER_TYPES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )
    type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return self.username
    
class House(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()
    sold = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey('House', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    reply = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.house.name} - {self.date}"



