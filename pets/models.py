from django.db import models
from django.conf import settings
from django.db import models


# Create your models here.
class Pet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    image = models.ImageField(upload_to='pet_images/', null=True, blank=True)

    def __str__(self):
        return self.name
