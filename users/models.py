from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
from users.utility import upload_user_image


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(TimeStamp):
    DOCTOR = 'doctor'
    PATIENT = 'patient'
    role_choices = [
        (PATIENT, PATIENT),
        (DOCTOR, DOCTOR),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    role = models.CharField(choices=role_choices, max_length=10)
