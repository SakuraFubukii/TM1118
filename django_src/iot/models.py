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
    time = models.DateTimeField()

    #Methods
    def __str__(self):
        return 'Event #{}'.format(self.id)
    
class tm1118_log(models.Model):
    #Fields
    node_id = models.TextField()
    loc = models.TextField()
    temp = models.IntegerField()
    hum = models.IntegerField()
    light = models.IntegerField()
    snd = models.IntegerField()
    date_created = models.TextField()

    #Methods
    def __str__(self):
        return 'tm1118_log #{}'.format(self.id)

class Step(models.Model):
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)