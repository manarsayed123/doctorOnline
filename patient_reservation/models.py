from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from doctor_time_slot.models import DoctorClinicTimeSlot
from users.models import TimeStamp


class Reservation(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='patient_reservation')
    doctor_clinic_appointment = models.ForeignKey(DoctorClinicTimeSlot, on_delete=models.PROTECT)
