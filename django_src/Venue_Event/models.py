from django.db import models

class Event(models.Model):
    venue = models.CharField(max_length=100)
    time_start = models.TimeField()
    time_end = models.TimeField()
    event_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)