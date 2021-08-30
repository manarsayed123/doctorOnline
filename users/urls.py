from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import Registeration

urlpatterns = [
    path('register/', Registeration.as_view(), name='register'),

]