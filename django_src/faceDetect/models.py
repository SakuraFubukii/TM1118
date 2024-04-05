from django.db import models

class Event(models.Model):
    #Fields
    people_num = models.DecimalField(max_digits=5, decimal_places=2)

    #Methods
    def __str__(self):
        return 'Event #{}'.format(self.id)