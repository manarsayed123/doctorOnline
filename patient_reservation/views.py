from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from patient_reservation.models import Reservation
from patient_reservation.serializers import ReservationSerializer


class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        doctor_clinic_appointment = serializer.validated_data['doctor_clinic_appointment']
        doctor_clinic_appointment.is_reserved = True
        doctor_clinic_appointment.save()
        serializer.save()

    def perform_update(self, serializer):
        doctor_clinic_appointment = serializer.validated_data['doctor_clinic_appointment']
        doctor_clinic_appointment.is_reserved = False
        doctor_clinic_appointment.save()
        serializer.save()

    def perform_destroy(self, instance):
        old_doctor_clinic_appointment = instance.doctor_clinic_appointment
        old_doctor_clinic_appointment.is_reserved = False
        old_doctor_clinic_appointment.save()
