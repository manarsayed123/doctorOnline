import logging

from django.core.management.base import BaseCommand

from doctor_time_slot.models import TimeSlot


class Command(BaseCommand):
    help = 'create time slots'

    def handle(self, *args, **options):
        for index in range(1, 13):
            try:
                TimeSlot.objects.create(time=index, am_or_pm="AM")
                TimeSlot.objects.create(time=index, am_or_pm="PM")
            except:
                pass

        print("Done time slot Creation")
