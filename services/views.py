from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminOrVet
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:  # Owners can view their appointments
            return [IsAuthenticated()]
        return [IsAdminOrVet()]  # Only Admins/Vets can create/update/delete

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Set the logged-in user as owner
