from django.urls import path, include
from rest_framework.routers import DefaultRouter

from patient_reservation.views import ReservationViewSet

router = DefaultRouter()
router.register('patient-reservation', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls)),

]
