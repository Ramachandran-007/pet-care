from rest_framework import serializers
from .models import MedicalRecord

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user
        if user.role not in ['Admin', 'Vet']:  # Ensure only Admins & Vets can edit
            raise serializers.ValidationError("You are not authorized to modify this data.")
        return data