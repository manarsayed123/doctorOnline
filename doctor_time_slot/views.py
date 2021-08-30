from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from doctorOnline.custom_permission_classes import IsDoctor
from doctor_time_slot.models import Clinic, DoctorClinicTimeSlot
from doctor_time_slot.serializers import ClinicSerializer, DoctorClinicTimeSlotSerializer
from django_filters.rest_framework import DjangoFilterBackend

from reversion.views import RevisionMixin


class ClinicViewSet(RevisionMixin, ModelViewSet):
    permission_classes = [IsDoctor]
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()


class DoctorClinicTimeSlotViewSet(RevisionMixin, ModelViewSet):
    permission_classes = [IsDoctor]
    serializer_class = DoctorClinicTimeSlotSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['is_reserved']

    def get_queryset(self):
        return DoctorClinicTimeSlot.objects.filter(user=self.request.user)
