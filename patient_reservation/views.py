from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from reversion.views import RevisionMixin

from doctorOnline.custom_permission_classes import IsPatient
from doctor_time_slot.models import DoctorClinicTimeSlot
from doctor_time_slot.serializers import DoctorClinicTimeSlotSerializer
from patient_reservation.models import Reservation
from patient_reservation.serializers import ReservationSerializer
import datetime
from rest_framework.generics import ListAPIView


class ReservationViewSet(RevisionMixin, ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [IsPatient]

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
        instance.is_deleted = True
        instance.deleted_at = datetime.datetime.now()
        instance.save()


class ListDoctorAvailableSlots(ListAPIView):
    permission_classes = [IsPatient]
    serializer_class = DoctorClinicTimeSlotSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user__username', 'clinic__name']

    def get_queryset(self):
        return DoctorClinicTimeSlot.objects.filter(is_reserved=False)
