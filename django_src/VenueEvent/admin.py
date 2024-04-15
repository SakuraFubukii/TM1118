from django.contrib import admin

# import Entry model
from .models import Event
from .models import Step

# Register your models here.
admin.site.register(Event)
admin.site.register(Step)