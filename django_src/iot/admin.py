from django.contrib import admin
from .models import Event
from .models import tm1118_log
from .models import Step
admin.site.register(Event)
admin.site.register(tm1118_log)
admin.site.register(Step)
# Register your models here.
