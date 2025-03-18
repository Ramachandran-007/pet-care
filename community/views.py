from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import LostFoundPet
from .serializers import LostFoundPetSerializer

class LostFoundPetViewSet(viewsets.ModelViewSet):
    queryset = LostFoundPet.objects.all()
    serializer_class = LostFoundPetSerializer