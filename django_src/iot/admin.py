from django.contrib import admin
from .models import Event
from .models import Step
from .models import Alert
admin.site.register(Event)
admin.site.register(Step)
admin.site.register(Alert)
# Register your models here.
