from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.
from doctor_time_slot.models import Clinic, TimeSlot, DoctorClinicTimeSlot
from patient_reservation.models import Reservation
from users.models import Profile


class TestReservation(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.patient = User.objects.create(username='patient', email='mnn@s.com', is_active=True)
        self.patient.set_password('1234')
        self.patient.save()
        Profile.objects.create(user=self.patient, role=Profile.PATIENT)
        self.doctor = User.objects.create(username='doctor', email='mnn@s.com', is_active=True)
        self.doctor.set_password('1234')
        self.doctor.save()
        Profile.objects.create(user=self.doctor, role=Profile.DOCTOR)
        start_time = TimeSlot.objects.create(time=2, am_or_pm='AM')
        end_time = TimeSlot.objects.create(time=1, am_or_pm='PM')
        time_slot = TimeSlot.objects.create(time=5, am_or_pm='PM')

        clinic = Clinic.objects.create(name='el salam2', week_days=['saturday', 'sunday'], start_time=start_time,
                                       end_time=end_time)
        self.doctor_clinic_time_slot = DoctorClinicTimeSlot.objects.create(clinic=clinic, time_slot=start_time,
                                                                           price=300, user=self.doctor,
                                                                           is_reserved=False)
        self.doctor_clinic_time_slot2 = DoctorClinicTimeSlot.objects.create(clinic=clinic, time_slot=end_time,
                                                                            price=400, user=self.doctor,
                                                                            is_reserved=False)
        self.doctor_clinic_time_slot3 = DoctorClinicTimeSlot.objects.create(clinic=clinic, time_slot=time_slot,
                                                                            price=400, user=self.doctor,
                                                                            is_reserved=True)

    def test_try_to_reserve_with_doctor_role(self):
        self.client.login(username='doctor', password='1234')
        response = self.client.post('/patient-reservation/',
                                    data={'doctor_clinic_appointment': self.doctor_clinic_time_slot})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_try_to_reserve_with_patient_role(self):
        self.client.login(username='patient', password='1234')
        self.client.post('/patient-reservation/',
                         data={'doctor_clinic_appointment': self.doctor_clinic_time_slot.id,
                               'user': self.patient})
        self.assertEqual(Reservation.objects.all().count(), 1)

    def test_doctor_clinic_slot_became_reserved_after_reservation(self):
        self.client.login(username='patient', password='1234')
        self.client.post('/patient-reservation/',
                         data={'doctor_clinic_appointment': self.doctor_clinic_time_slot2.id,
                               'user': self.patient})
        self.assertEqual(Reservation.objects.last().doctor_clinic_appointment.is_reserved, True)

    def test_reservation_with_unavailable_time(self):
        self.client.login(username='patient', password='1234')
        response = self.client.post('/patient-reservation/',
                                    data={'doctor_clinic_appointment': self.doctor_clinic_time_slot3.id,
                                          'user': self.patient})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
