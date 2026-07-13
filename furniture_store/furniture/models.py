from django.db import models

# Create your models here.
class Stock(models.Model):
    name=models.CharField(max_length=100)
    types=[
    ('CHAIR', 'Chair'),
    ('TABLE', 'Table'),
    ('BED', 'Bed'),
    ('SOFA', 'Sofa'),
    ('WARDROBE', 'Wardrobe'),
    ('CABINET', 'Cabinet / Storage'),
    ('DINING', 'Dining Set'),
    ('OFFICE', 'Office Desk'),]
    FURNITURE_TYPES = models.CharField(choices=types)
    description=models.TextField(max_length=500)
    img=models.ImageField(upload_to='stocks/')
    price=models.FloatField()
    def __str__(self):
        return self.name
    

from django.db import models
from django.contrib.auth.models import User # <-- 1. Add this import at the top!

# ... (Your existing Product model and FURNITURE_TYPES are here) ...

# 2. Add the UserProfile model
class UserProfile(models.Model):
    # This links your custom profile to the standard Django user system
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ph_no = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)
    user_no = models.CharField(max_length=50, unique=True) 

    def __str__(self):
        return f"{self.user.username}'s Profile"