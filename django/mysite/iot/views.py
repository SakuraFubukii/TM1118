from django.shortcuts import render
from . import iot_mqtt
from .models import Event
# Create your views here.
def index(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'iot/index.html', context)