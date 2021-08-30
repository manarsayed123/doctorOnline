from rest_framework import serializers

from doctor_time_slot.serializers import DoctorClinicTimeSlotSerializer
from patient_reservation.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reservation
        fields = '__all__'