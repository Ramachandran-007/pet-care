from django.contrib.auth.models import AbstractUser, Group, Permission
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

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Change related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Change related_name
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

