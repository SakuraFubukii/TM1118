from django.db import models

# Create your models here.
class Event(models.Model):
    #Fields
    node_id = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    hum = models.DecimalField(max_digits=5, decimal_places=2)
    light = models.DecimalField(max_digits=5, decimal_places=2)
    snd = models.DecimalField(max_digits=5, decimal_places=2)

    #Methods
    def __str__(self):
        return 'Event #{}'.format(self.id)