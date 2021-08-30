from rest_framework import serializers

from doctor_time_slot.models import Clinic, DoctorClinicTimeSlot

from multiselectfield import MultiSelectField


class ClinicSerializer(serializers.ModelSerializer):
    week_days = MultiSelectField(choices=Clinic.WEEK_DAYS_CHOICES)

    class Meta:
        model = Clinic
        exclude = ('deleted_at', 'is_deleted')


class DoctorClinicTimeSlotSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = DoctorClinicTimeSlot
        exclude = ('deleted_at', 'is_deleted')

