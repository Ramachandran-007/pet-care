from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    image = models.ImageField(upload_to='pet_images/', null=True, blank=True)

    def __str__(self):
        return self.name
