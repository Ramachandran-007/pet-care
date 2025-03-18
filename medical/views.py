from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from users.permissions import IsAdminOrVet
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [[IsAdminOrVet]]