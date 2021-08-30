from rest_framework import serializers

from doctor_time_slot.models import DoctorClinicTimeSlot
from doctor_time_slot.serializers import DoctorClinicTimeSlotSerializer
from patient_reservation.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    doctor_clinic_appointment = serializers.PrimaryKeyRelatedField(
        queryset=DoctorClinicTimeSlot.objects.filter(is_reserved=False))

    class Meta:
        model = Reservation
        # fields = '__all__'
        exclude = ('deleted_at', 'is_deleted')
