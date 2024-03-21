from django.db import models

# Create your models here.
class Entry(models.Model):
#Fields
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    #Methods
    def __str__(self):
        return 'Entry #{}'.format(self.id)