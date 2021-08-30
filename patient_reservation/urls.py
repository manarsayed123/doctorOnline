from django.urls import path, include
from rest_framework.routers import DefaultRouter

from patient_reservation.views import ReservationViewSet, ListDoctorAvailableSlots

router = DefaultRouter()
router.register('patient-reservation', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls)),
    path('doctor-available-appointments/', ListDoctorAvailableSlots.as_view(), name='doctor_available_slots'),


]
