from django.db import models
from pets.models import Pet

# Create your models here.
class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=[
        ('Grooming', 'Grooming'),
        ('Training', 'Training'),
        ('Veterinary', 'Veterinary'),
    ])
    date = models.DateTimeField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.pet.name} - {self.service_type} on {self.date}"
