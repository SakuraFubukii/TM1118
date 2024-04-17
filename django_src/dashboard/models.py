from django.db import models

# Create your models here.

class Event(models.Model): #Fields
    node_id = models.CharField(max_length=5)
    node_loc = models.CharField(max_length=10)
    temp = models.IntegerField()
    hum = models.IntegerField()
    light = models.IntegerField()
    snd = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    
    #Methods
    def __str__(self):
        return 'Event #{}'.format(self.id)