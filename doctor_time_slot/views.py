from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from doctor_time_slot.models import Clinic, DoctorClinicTimeSlot
from doctor_time_slot.serializers import ClinicSerializer, DoctorClinicTimeSlotSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ClinicViewSet(ModelViewSet):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()


class DoctorClinicTimeSlotViewSet(ModelViewSet):
    serializer_class = DoctorClinicTimeSlotSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['is_reserved']



    def get_queryset(self):
        return DoctorClinicTimeSlot.objects.filter(user=self.request.user)


