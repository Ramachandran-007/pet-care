from django.db import models
from django.conf import settings
from django.db import models
from pets.models import Pet

# Create your models here.
class LostFoundPet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('Lost', 'Lost'), ('Found', 'Found')])
    location = models.CharField(max_length=255)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet.name} - {self.status}"
