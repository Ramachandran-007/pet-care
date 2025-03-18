from django.db import models
from pets.models import Pet

# Create your models here.
class MedicalRecord(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    record_date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField()
    prescription = models.TextField()
    vet_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pet.name} - {self.record_date}"
