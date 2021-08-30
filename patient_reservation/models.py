from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django_softdelete.models import SoftDeleteModel

from doctor_time_slot.models import DoctorClinicTimeSlot
from users.models import TimeStamp
import reversion


@reversion.register()
class Reservation(TimeStamp, SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='patient_reservation')
    doctor_clinic_appointment = models.ForeignKey(DoctorClinicTimeSlot, on_delete=models.PROTECT)

    class Meta:
        unique_together = ['user', 'doctor_clinic_appointment', 'deleted_at']
        ordering = ['-id']
