from django.urls import path, include
from rest_framework.routers import DefaultRouter

from doctor_time_slot.views import ClinicViewSet, DoctorClinicTimeSlotViewSet

router = DefaultRouter()
router.register('clinic', ClinicViewSet, basename='clinic_crud')
router.register('doctor-clinic-time-slot', DoctorClinicTimeSlotViewSet, basename='doctor_clinic_time_slot_crud')

urlpatterns = [
    path('', include(router.urls)),

]
