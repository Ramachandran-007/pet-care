from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Vet', 'Vet'),
        ('PetOwner', 'PetOwner'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='PetOwner')
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
