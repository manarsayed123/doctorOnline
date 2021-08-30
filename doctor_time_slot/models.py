from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import TimeStamp


class TimeSlot(models.Model):
    AM_OR_PM_CHOICES = (
        ("AM", "AM"),
        ("PM", "PM"),
    )
    time = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    am_or_pm = models.CharField(max_length=2, choices=AM_OR_PM_CHOICES)

    class Meta:
        unique_together = ('time', 'am_or_pm')
        ordering = ['time', 'am_or_pm', 'id']

    def __str__(self):
        return f'{self.time} {self.am_or_pm}'


class Clinic(TimeStamp):
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    WEEK_DAYS_CHOICES = (
        (SATURDAY, SATURDAY),
        (SUNDAY, SUNDAY),
        (MONDAY, MONDAY),
        (TUESDAY, TUESDAY),
        (WEDNESDAY, WEDNESDAY),
        (THURSDAY, THURSDAY),
        (FRIDAY, FRIDAY),
    )
    name = models.CharField(max_length=255)
    start_time = models.ForeignKey(TimeSlot, on_delete=models.PROTECT, related_name='clinic_start_time')
    end_time = models.ForeignKey(TimeSlot, on_delete=models.PROTECT, related_name='clinic_end_time')
    week_days = MultiSelectField(choices=WEEK_DAYS_CHOICES, blank=True, null=True)
    user = models.ManyToManyField(User, through="DoctorClinicTimeSlot")


class DoctorClinicTimeSlot(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT)
    price = models.FloatField()
    is_reserved = models.BooleanField(default=False)
