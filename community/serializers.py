from rest_framework import serializers
from .models import LostFoundPet

class LostFoundPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostFoundPet
        fields = '__all__'
